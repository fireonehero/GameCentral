import math
import pygame
import games.top_down_shooter.sounds as sounds
import games.top_down_shooter.settings as settings

def update_bullets(bullets, enemies, walls):
    for bullet in bullets[:]:
        bullet[0] += bullet[2]  # x += vx
        bullet[1] += bullet[3]  # y += vy

        bullet_rect = pygame.Rect(bullet[0] - 2, bullet[1] - 2, 4, 4)

        # Check collision with walls
        if any(bullet_rect.colliderect(wall) for wall in walls):
            sounds.bullet_impact_wall.play()
            bullet[4] -= 1  # reduce penetration
            if bullet[4] <= 0:
                bullets.remove(bullet)
            continue  # Don't check enemies this frame

        # Check collision with enemies
        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy['x'] - 16, enemy['y'] - 16, 32, 32)
            if bullet_rect.colliderect(enemy_rect):
                sounds.hitmarker.play()
                enemy['health'] -= settings.DAMAGE
                bullet[4] -= 1
                if bullet[4] <= 0:
                    bullets.remove(bullet)
                break  # one enemy hit per frame


def draw_bullets(screen, bullets, camera_x, camera_y):
    for b in bullets:
        x, y, vx, vy, force = b
        angle = math.degrees(math.atan2(vy, vx))

        # Create bullet surface
        bullet_width = 12
        bullet_height = 1
        bullet_surf = pygame.Surface((bullet_width, bullet_height), pygame.SRCALPHA)
        pygame.draw.rect(bullet_surf, (255, 255, 0), (0, 0, bullet_width, bullet_height), border_radius=3)

        # Rotate bullet to match direction
        rotated_surf = pygame.transform.rotate(bullet_surf, -angle)
        rotated_rect = rotated_surf.get_rect(center=(x - camera_x, y - camera_y))

        screen.blit(rotated_surf, rotated_rect.topleft)
