import games.top_down_shooter.settings as settings

def draw_ammo_info(screen, font, width):
    if settings.IS_RELOADING:
        text = f"Reloading..."
    else:
        text = f"{settings.AMMO_COUNT}/{settings.AMMO_CAPACITY}"
    display = font.render(f"Weapon {settings.EQUIPPED} Ammo {text}", True, (255, 255, 255))
    screen.blit(display, display.get_rect(topright=(width - 10, 10)))
def draw_game_over_text(screen, font):
    text = "GAME OVER"
    display = font.render(text, True, (155, 25, 25))
    screen.blit(display, display.get_rect(center=(settings.WIDTH//2, settings.HEIGHT//2)))
def draw_health_text(screen, font):
    text = f'Health: {settings.PLAYER_HEALTH}/100'
    display = font.render(text, True, (155, 25, 25))
    screen.blit(display, display.get_rect(topleft=(10, 10)))
def draw_score_text(screen, font):
    text = f'{settings.SCORE}'
    display = font.render(text, True, (255, 255, 255))
    screen.blit(display, display.get_rect(midtop=(settings.WIDTH//2, 10)))