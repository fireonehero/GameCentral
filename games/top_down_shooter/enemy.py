import pygame
import random

import games.top_down_shooter.settings as settings
import math

def spawn_enemies(count, width, height):
    enemies = []
    for _ in range(count):
        x = random.randint(-width, width)
        y = random.randint(-height, height)
        enemies.append({
            "x": x,
            "y": y,
            "radius": 25,
            "health": 100,
            "path": [(100, 100), (700, 100)],
            "path_index": 0,
            "speed": settings.ENEMY_SPEED,
            "attack_speed": 2000,  # milliseconds
            "last_attack_time": 0 
        })
    return enemies

def spawn_single_enemy(width, height):
    x = random.randint(-width, width)
    y = random.randint(-height, height)
    return {'x': x, 'y': y, 'radius': 25, 'health': 100, 'path': [], 'path_index': 0, 'speed': settings.ENEMY_SPEED, "attack_speed": 2000, "last_attack_time": 0}

def move_enemy_along_path(enemy):
    if not enemy["path"]:
        return  # no path to follow

    target_x, target_y = enemy["path"][enemy["path_index"]]
    dx = target_x - enemy["x"]
    dy = target_y - enemy["y"]
    distance = math.hypot(dx, dy)

    if distance < enemy["speed"]:
        # Reached the target, go to next waypoint
        enemy["x"] = target_x
        enemy["y"] = target_y
        enemy["path_index"] = (enemy["path_index"] + 1) % len(enemy["path"])
    else:
        # Normalize direction and move
        enemy["x"] += (dx / distance) * enemy["speed"]
        enemy["y"] += (dy / distance) * enemy["speed"]

def move_enemy_towards_player(enemy, player_pos, walls, enemies):
    dx = player_pos[0] - enemy['x']
    dy = player_pos[1] - enemy['y']
    distance = math.hypot(dx, dy)

    if distance == 0:
        return

    dx /= distance
    dy /= distance

    step_x = dx * enemy['speed']
    step_y = dy * enemy['speed']

    # Try moving along x axis
    new_x = enemy['x'] + step_x
    enemy_rect_x = pygame.Rect(new_x - 16, enemy['y'] - 16, 32, 32)
    if not any(enemy_rect_x.colliderect(wall) for wall in walls) and not any(
        enemy_rect_x.colliderect(pygame.Rect(other['x'] - 16, other['y'] - 16, 32, 32))
        for other in enemies if other != enemy):
        enemy['x'] = new_x

    # Try moving along y axis
    new_y = enemy['y'] + step_y
    enemy_rect_y = pygame.Rect(enemy['x'] - 16, new_y - 16, 32, 32)
    if not any(enemy_rect_y.colliderect(wall) for wall in walls) and not any(
        enemy_rect_y.colliderect(pygame.Rect(other['x'] - 16, other['y'] - 16, 32, 32))
        for other in enemies if other != enemy):
        enemy['y'] = new_y

def draw_enemies(screen, enemies, camera_x, camera_y):
    for enemy in enemies:
        pygame.draw.circle(screen, (0, 0, 0), (int(enemy["x"] - camera_x), int(enemy["y"] - camera_y)), enemy["radius"] + 2.5)
        pygame.draw.circle(screen, (255, 0, 0), (int(enemy["x"] - camera_x), int(enemy["y"] - camera_y)), enemy["radius"])

def handle_player_overlap(player_rect, enemies):
    now = pygame.time.get_ticks()
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy['x'] - enemy['radius'], enemy['y'] - enemy['radius'], enemy['radius'] * 2, enemy['radius'] * 2)
        if enemy_rect.colliderect(player_rect):
            if now - enemy["last_attack_time"] >= enemy["attack_speed"]:
                settings.PLAYER_HEALTH -= random.randint(10, 25)
                enemy["last_attack_time"] = now