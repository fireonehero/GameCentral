import pygame
import games.top_down_shooter.settings as settings

pygame.mixer.init()
pygame.mixer.set_num_channels(32)

dry_fire = pygame.mixer.Sound("games\\top_down_shooter\\assets\sounds\sfx\empty-trigger-pull.wav")
hitmarker = pygame.mixer.Sound("games\\top_down_shooter\\assets\sounds\sfx\hitmarker.wav")
bullet_impact_wall = pygame.mixer.Sound("games\\top_down_shooter\\assets\sounds\sfx\\bullet_impact_wall.wav")

def update_gunshot_sound():
    global gunshot
    gunshot = pygame.mixer.Sound(settings.GUNSHOT_SOUND)
    gunshot.set_volume(1.0)

def update_reload_sound():
    global reload
    reload = pygame.mixer.Sound(settings.RELOAD_SOUND)
    reload.set_volume(1.0)

dry_fire.set_volume(0.5)
hitmarker.set_volume(0.5)
bullet_impact_wall.set_volume(0.5)