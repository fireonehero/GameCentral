import pygame, random, math
import games.top_down_shooter.settings as settings
import games.top_down_shooter.guns as guns
import games.top_down_shooter.sounds as sounds
import games.top_down_shooter.squares as squares

from games.top_down_shooter.player import draw_player, get_angle_to_mouse
from games.top_down_shooter.enemy import spawn_enemies, draw_enemies, move_enemy_towards_player, spawn_single_enemy, handle_player_overlap
from games.top_down_shooter.bullet import update_bullets, draw_bullets
from games.top_down_shooter.ui import draw_ammo_info, draw_game_over_text, draw_health_text

def play_top_down_shooter():
    pygame.init()
    pygame.font.init()

    # Screen setup
    WIDTH, HEIGHT = settings.WIDTH, settings.HEIGHT
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Fonts
    font_path = "games\\top_down_shooter\\assets/fonts"
    gun_font = pygame.font.Font(f"{font_path}/Hardcore Imperial.ttf", 30)
    game_over_font = pygame.font.Font(f"{font_path}/Zombified.ttf", 72)
    health_font = pygame.font.Font(f"{font_path}/Hardcore Imperial.ttf", 30)

    # Game state
    player_pos = [WIDTH // 2, HEIGHT // 2]
    camera_x = player_pos[0] - WIDTH // 2
    camera_y = player_pos[1] - HEIGHT // 2
    player_rect = pygame.Rect(0, 0, settings.PLAYER_RADIUS * 2, settings.PLAYER_RADIUS * 2)

    bullets = []
    enemies = spawn_enemies(5, WIDTH, HEIGHT)

    mouse_held = False
    last_shot_time = 0

    next_enemy_spawn_delay = random.randint(*settings.ENEMY_SPAWN_RATE)
    enemy_spawn_timer = 0

    running = True
    while running:
        dt = clock.tick(120)
        screen.fill((0, 20, 0))

        # Camera follow
        camera_x = player_pos[0] - WIDTH // 2
        camera_y = player_pos[1] - HEIGHT // 2
        player_rect.topleft = (player_pos[0] - settings.PLAYER_RADIUS, player_pos[1] - settings.PLAYER_RADIUS)

        # Spawn enemies over time
        enemy_spawn_timer += dt
        if enemy_spawn_timer >= next_enemy_spawn_delay:
            enemies.extend(spawn_enemies(random.randint(3, 8), WIDTH, HEIGHT))
            enemy_spawn_timer = 0
            next_enemy_spawn_delay = random.randint(5000, 10000)

        # Player movement
        keys = pygame.key.get_pressed()
        speed = settings.PLAYER_SPEED * 1.75 if keys[pygame.K_LSHIFT] else settings.PLAYER_SPEED
        dx = dy = 0
        if settings.PLAYER_HEALTH > 0:
            dx = (keys[pygame.K_d] - keys[pygame.K_a]) * speed
            dy = (keys[pygame.K_s] - keys[pygame.K_w]) * speed

        new_rect_x = player_rect.move(dx, 0)
        if not any(new_rect_x.colliderect(wall) for wall in squares.wall_squares):
            player_pos[0] += dx

        new_rect_y = player_rect.move(0, dy)
        if not any(new_rect_y.colliderect(wall) for wall in squares.wall_squares):
            player_pos[1] += dy

        # Handle game elements
        squares.handle_gun_square_overlap(player_rect)

        if settings.PLAYER_HEALTH > 0:
            draw_player(screen, (WIDTH // 2, HEIGHT // 2), get_angle_to_mouse(player_pos))
            handle_player_overlap(player_rect, enemies)

        squares.draw_gun_squares(camera_x, camera_y, screen)
        squares.draw_wall_squares(camera_x, camera_y, screen)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_held = True
                if settings.PLAYER_HEALTH > 0 and not settings.IS_RELOADING and settings.AMMO_COUNT == 0:
                    sounds.dry_fire.play()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_held = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                settings.PLAYER_SPEED /= 2
                if settings.EQUIPPED != "none":
                    settings.BULLET_INACCURACY /= 2
                else:
                    print('No gun selected')
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                settings.PLAYER_SPEED *= 2
                if settings.EQUIPPED != "none":
                    settings.BULLET_INACCURACY *= 2
                else:
                    print('No gun selected')

        # Reloading
        now = pygame.time.get_ticks()
        if keys[pygame.K_r] and not settings.IS_RELOADING and settings.AMMO_COUNT < settings.AMMO_CAPACITY and settings.PLAYER_HEALTH > 0:
            settings.IS_RELOADING = True
            reload_start = now
            settings.RELOAD_SOUND = guns.gun_data[settings.EQUIPPED]["reload_sound"]
            sounds.update_reload_sound()
            if settings.EQUIPPED == "Remington 870":
                bullets_needed = settings.AMMO_CAPACITY - settings.AMMO_COUNT
                settings.RELOAD_TIME = guns.gun_data["Remington 870"]["reload_time"] * bullets_needed
                sounds.reload.play(loops=bullets_needed - 1)
            else:
                settings.RELOAD_TIME = guns.gun_data[settings.EQUIPPED]["reload_time"]
                sounds.reload.play()

        if settings.IS_RELOADING and now - reload_start >= settings.RELOAD_TIME * 1000:
            settings.AMMO_COUNT = settings.AMMO_CAPACITY
            settings.IS_RELOADING = False

        # Shooting
        if settings.EQUIPPED != "none" and mouse_held and settings.AMMO_COUNT > 0 and not settings.IS_RELOADING:
            delay = guns.gun_data[settings.EQUIPPED]['firing_delay'] * 1000
            if now - last_shot_time >= delay:
                settings.AMMO_COUNT -= 1
                sounds.gunshot.play()
                spread = math.radians(settings.BULLET_INACCURACY)
                for _ in range(guns.gun_data[settings.EQUIPPED]['projectiles']):
                    angle = get_angle_to_mouse(player_pos) + random.uniform(-spread, spread)
                    vx, vy = math.cos(angle) * settings.BULLET_SPEED, math.sin(angle) * settings.BULLET_SPEED
                    bullets.append([player_pos[0], player_pos[1], vx, vy, settings.PENETRATION])
                last_shot_time = now

        # Update and draw
        update_bullets(bullets, enemies, squares.wall_squares)
        enemies[:] = [e for e in enemies if e['health'] > 0]
        for enemy in enemies:
            move_enemy_towards_player(enemy, player_pos, squares.wall_squares, enemies)

        draw_bullets(screen, bullets, camera_x, camera_y)
        draw_enemies(screen, enemies, camera_x, camera_y)
        draw_ammo_info(screen, gun_font, WIDTH)
        draw_health_text(screen, health_font)

        if settings.PLAYER_HEALTH <= 0:
            draw_game_over_text(screen, game_over_font)

        pygame.display.flip()

    pygame.quit()