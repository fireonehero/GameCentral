import pygame

import games.top_down_shooter.settings as settings
import games.top_down_shooter.sounds as sounds
import games.top_down_shooter.guns as guns

HEIGHT, WIDTH = settings.HEIGHT, settings.WIDTH

gun_squares = [pygame.Rect(i * settings.WIDTH//5, settings.HEIGHT - 50, settings.WIDTH//5, 50) for i in range(5)]
gun_square_colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 200, 0), (200, 0, 200)]

wall_squares = [pygame.Rect(-WIDTH, -HEIGHT, 25, HEIGHT*3), pygame.Rect(-WIDTH, -HEIGHT, WIDTH*3, 25), pygame.Rect(WIDTH*2, -HEIGHT, 25, (HEIGHT*3)+25), pygame.Rect(-WIDTH, HEIGHT*2, WIDTH*3, 25)]
wall_square_colors = [(50, 30, 10), (50, 30, 10), (50, 30, 10), (50, 30, 10)]

def draw_gun_squares(camera_x, camera_y, screen):
    for i, rect in enumerate(gun_squares):
        screen_rect = rect.move(-camera_x, -camera_y)
        pygame.draw.rect(screen, gun_square_colors[i], screen_rect)

def draw_wall_squares(camera_x, camera_y, screen):
    for i, rect in enumerate(wall_squares):
        screen_rect = rect.move(-camera_x, -camera_y)
        pygame.draw.rect(screen, wall_square_colors[i], screen_rect)

def handle_gun_square_overlap(player_rect):
    for i, square in enumerate(gun_squares):
        if player_rect.colliderect(square):
            names = ["M1911", "MP5", "M4A1", "Remington 870", "AWP"]
            settings.EQUIPPED = names[i]
            gun = guns.gun_data[settings.EQUIPPED]
            settings.BULLET_SPEED = gun['bullet_speed']
            settings.BULLET_INACCURACY = gun['bullet_inaccuracy']
            settings.AMMO_CAPACITY = gun['ammo_capacity']
            settings.AMMO_COUNT = gun['ammo_capacity']
            settings.DAMAGE = gun['damage']
            settings.PENETRATION = gun['penetration']
            settings.GUNSHOT_SOUND = gun['gunshot_sound']
            sounds.update_gunshot_sound()