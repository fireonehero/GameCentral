import pygame
import random

import games.top_down_shooter.settings as settings
import games.top_down_shooter.sounds as sounds
import games.top_down_shooter.guns as guns

HEIGHT, WIDTH = settings.HEIGHT, settings.WIDTH

gun_squares = [pygame.Rect(i * settings.WIDTH//5, settings.HEIGHT - 50, settings.WIDTH//5, 50) for i in range(5)]
gun_square_colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 200, 0), (200, 0, 200)]
box_squares = [pygame.Rect(2 * WIDTH//5, HEIGHT - 50, WIDTH//5, 50)]
box_square_colors = [(85, 65, 40)]

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

def draw_random_box_square(camera_x, camera_y, screen):
    for i, rect in enumerate(box_squares):
        screen_rect = rect.move(-camera_x, -camera_y)
        pygame.draw.rect(screen, box_square_colors[i], screen_rect)

def handle_gun_square_overlap(player_rect):
    for i, square in enumerate(gun_squares):
        if player_rect.colliderect(square):
            names = ["M1911", "MP5", "M4A1", "Remington 870", "AWP"]
            settings.EQUIPPED = names[i]
            guns.new_equip(settings.EQUIPPED)

def handle_random_box_overlap(player_rect):
    now = pygame.time.get_ticks()
    names = [*guns.gun_data]
    if player_rect.colliderect(box_squares[0]) and settings.SCORE >= 250:
        if now - settings.BOX_LAST_HIT >= settings.BOX_REFRESH_SPEED:
            print("hitting the box")
            settings.EQUIPPED = random.choice(names)
            guns.new_equip(settings.EQUIPPED)
            settings.BOX_LAST_HIT = now
            settings.SCORE -= 250