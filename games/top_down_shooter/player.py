import math
import pygame

import games.top_down_shooter.settings as settings

def get_angle_to_mouse(pos):
    mx, my = pygame.mouse.get_pos()
    # Convert mouse screen coords to world coords
    world_mouse_x = mx + (pos[0] - settings.WIDTH // 2)
    world_mouse_y = my + (pos[1] - settings.HEIGHT // 2)
    return math.atan2(world_mouse_y - pos[1], world_mouse_x - pos[0])


def draw_player(screen, pos, angle):
    length = 40
    end_x = pos[0] + math.cos(angle) * length
    end_y = pos[1] + math.sin(angle) * length
    pygame.draw.circle(screen, (0, 0, 0), pos, settings.PLAYER_RADIUS + 2.5)
    pygame.draw.circle(screen, (0, 255, 0), pos, settings.PLAYER_RADIUS)
    pygame.draw.line(screen, (255, 0, 0), pos, (end_x, end_y), 4)
