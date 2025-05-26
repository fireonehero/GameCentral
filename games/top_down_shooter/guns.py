import math

import games.top_down_shooter.settings as settings
import games.top_down_shooter.sounds as sounds

gun_data = {
    # Handguns
    'M1911':          {'bullet_speed': math.sqrt(25.3)*2, 'damage': 45, 'projectiles': 1, 'bullet_inaccuracy': 5, 'firing_delay': 0.25, 'ammo_capacity': 7,  'reload_time': 0.75, 'penetration': 0, 'gunshot_sound': "assets/sounds/handgun/handgun_shot.wav", 'reload_sound': "assets/sounds/handgun/handgun_reload.wav"},
    'Glock 17':       {'bullet_speed': math.sqrt(37.5)*2, 'damage': 35, 'projectiles': 1, 'bullet_inaccuracy': 5, 'firing_delay': 0.15, 'ammo_capacity': 17, 'reload_time': 0.75, 'penetration': 0, 'gunshot_sound': "assets/sounds/handgun/handgun_shot.wav", 'reload_sound': "assets/sounds/handgun/handgun_reload.wav"},
    'Beretta M9':     {'bullet_speed': math.sqrt(38.1)*2, 'damage': 35, 'projectiles': 1, 'bullet_inaccuracy': 5, 'firing_delay': 0.20, 'ammo_capacity': 10, 'reload_time': 0.75, 'penetration': 0, 'gunshot_sound': "assets/sounds/handgun/handgun_shot.wav", 'reload_sound': "assets/sounds/handgun/handgun_reload.wav"},
    'Desert Eagle':   {'bullet_speed': math.sqrt(50.0)*2, 'damage': 90, 'projectiles': 1, 'bullet_inaccuracy': 4, 'firing_delay': 0.50, 'ammo_capacity': 7,  'reload_time': 0.75, 'penetration': 1, 'gunshot_sound': "assets/sounds/handgun/handgun_shot.wav", 'reload_sound': "assets/sounds/handgun/handgun_reload.wav"},
    'USP .45':        {'bullet_speed': math.sqrt(40.0)*2, 'damage': 40, 'projectiles': 1, 'bullet_inaccuracy': 4.5, 'firing_delay': 0.22, 'ammo_capacity': 12, 'reload_time': 0.75, 'penetration': 0, 'gunshot_sound': "assets/sounds/handgun/handgun_shot.wav", 'reload_sound': "assets/sounds/handgun/handgun_reload.wav"},

    # SMGs
    'MP5':            {'bullet_speed': math.sqrt(40.0)*2, 'damage': 35, 'projectiles': 1, 'bullet_inaccuracy': 7.5, 'firing_delay': 0.017, 'ammo_capacity': 30, 'reload_time': 0.85, 'penetration': 0, 'gunshot_sound': "assets/sounds/smg/smg_shot.wav", 'reload_sound': "assets/sounds/smg/smg_reload.wav"},
    'Uzi':            {'bullet_speed': math.sqrt(35.0)*2, 'damage': 30, 'projectiles': 1, 'bullet_inaccuracy': 9.0, 'firing_delay': 0.05,  'ammo_capacity': 32, 'reload_time': 0.85, 'penetration': 0, 'gunshot_sound': "assets/sounds/smg/smg_shot.wav", 'reload_sound': "assets/sounds/smg/smg_reload.wav"},
    'MAC-10':         {'bullet_speed': math.sqrt(33.0)*2, 'damage': 28, 'projectiles': 1, 'bullet_inaccuracy': 10.0, 'firing_delay': 0.04,  'ammo_capacity': 30, 'reload_time': 0.85, 'penetration': 0, 'gunshot_sound': "assets/sounds/smg/smg_shot.wav", 'reload_sound': "assets/sounds/smg/smg_reload.wav"},
    'P90':            {'bullet_speed': math.sqrt(42.0)*2, 'damage': 34, 'projectiles': 1, 'bullet_inaccuracy': 7.0, 'firing_delay': 0.06,  'ammo_capacity': 50, 'reload_time': 0.85, 'penetration': 1, 'gunshot_sound': "assets/sounds/smg/smg_shot.wav", 'reload_sound': "assets/sounds/smg/smg_reload.wav"},
    'Vector':         {'bullet_speed': math.sqrt(39.0)*2, 'damage': 32, 'projectiles': 1, 'bullet_inaccuracy': 6.5, 'firing_delay': 0.03,  'ammo_capacity': 25, 'reload_time': 0.85, 'penetration': 1, 'gunshot_sound': "assets/sounds/smg/smg_shot.wav", 'reload_sound': "assets/sounds/smg/smg_reload.wav"},

    # Rifles
    'M4A1':           {'bullet_speed': math.sqrt(88.0)*2, 'damage': 65, 'projectiles': 1, 'bullet_inaccuracy': 8, 'firing_delay': 0.077, 'ammo_capacity': 30, 'reload_time': 1.85, 'penetration': 0, 'gunshot_sound': "assets/sounds/assault_rifle/ar_shot.wav", 'reload_sound': "assets/sounds/assault_rifle/ar_reload.wav"},
    'AK-47':          {'bullet_speed': math.sqrt(85.0)*2, 'damage': 75, 'projectiles': 1, 'bullet_inaccuracy': 10, 'firing_delay': 0.10,  'ammo_capacity': 30, 'reload_time': 1.85, 'penetration': 1, 'gunshot_sound': "assets/sounds/assault_rifle/ar_shot.wav", 'reload_sound': "assets/sounds/assault_rifle/ar_reload.wav"},
    'FAMAS':          {'bullet_speed': math.sqrt(80.0)*2, 'damage': 60, 'projectiles': 1, 'bullet_inaccuracy': 7, 'firing_delay': 0.09,  'ammo_capacity': 25, 'reload_time': 1.85, 'penetration': 1, 'gunshot_sound': "assets/sounds/assault_rifle/ar_shot.wav", 'reload_sound': "assets/sounds/assault_rifle/ar_reload.wav"},
    'SCAR-L':         {'bullet_speed': math.sqrt(90.0)*2, 'damage': 80, 'projectiles': 1, 'bullet_inaccuracy': 6, 'firing_delay': 0.11,  'ammo_capacity': 20, 'reload_time': 1.85, 'penetration': 1, 'gunshot_sound': "assets/sounds/assault_rifle/ar_shot.wav", 'reload_sound': "assets/sounds/assault_rifle/ar_reload.wav"},
    'AUG':            {'bullet_speed': math.sqrt(85.0)*2, 'damage': 70, 'projectiles': 1, 'bullet_inaccuracy': 5.5, 'firing_delay': 0.08, 'ammo_capacity': 30, 'reload_time': 1.85, 'penetration': 1, 'gunshot_sound': "assets/sounds/assault_rifle/ar_shot.wav", 'reload_sound': "assets/sounds/assault_rifle/ar_reload.wav"},

    # Shotguns
    'Remington 870':  {'bullet_speed': math.sqrt(40.8)*2, 'damage': 25, 'projectiles': 12, 'bullet_inaccuracy': 10, 'firing_delay': 1.3, 'ammo_capacity': 5,  'reload_time': 0.91, 'penetration': 0, 'gunshot_sound': "assets/sounds/shotgun/shotgun_shot.wav", 'reload_sound': "assets/sounds/shotgun/shotgun_reload.wav"},
    'SPAS-12':        {'bullet_speed': math.sqrt(45.0)*2, 'damage': 22, 'projectiles': 10, 'bullet_inaccuracy': 9,  'firing_delay': 1.0, 'ammo_capacity': 8,  'reload_time': 0.91, 'penetration': 0, 'gunshot_sound': "assets/sounds/shotgun/shotgun_shot.wav", 'reload_sound': "assets/sounds/shotgun/shotgun_reload.wav"},
    'M1014':          {'bullet_speed': math.sqrt(48.0)*2, 'damage': 24, 'projectiles': 10, 'bullet_inaccuracy': 8.5,'firing_delay': 0.85,'ammo_capacity': 7,  'reload_time': 0.91,  'penetration': 0, 'gunshot_sound': "assets/sounds/shotgun/shotgun_shot.wav", 'reload_sound': "assets/sounds/shotgun/shotgun_reload.wav"},
    'KSG':            {'bullet_speed': math.sqrt(50.0)*2, 'damage': 26, 'projectiles': 12, 'bullet_inaccuracy': 9,  'firing_delay': 1.1, 'ammo_capacity': 14, 'reload_time': 0.91,  'penetration': 1, 'gunshot_sound': "assets/sounds/shotgun/shotgun_shot.wav", 'reload_sound': "assets/sounds/shotgun/shotgun_reload.wav"},
    'Double Barrel':  {'bullet_speed': math.sqrt(35.0)*2, 'damage': 30, 'projectiles': 16, 'bullet_inaccuracy': 11, 'firing_delay': 1.5, 'ammo_capacity': 2,  'reload_time': 0.91,  'penetration': 0, 'gunshot_sound': "assets/sounds/shotgun/shotgun_shot.wav", 'reload_sound': "assets/sounds/shotgun/shotgun_reload.wav"},

    # Sniper Rifles
    'AWP':            {'bullet_speed': math.sqrt(94.0)*2, 'damage': 100, 'projectiles': 1, 'bullet_inaccuracy': 1, 'firing_delay': 1.7, 'ammo_capacity': 5,  'reload_time': 0.91, 'penetration': 2, 'gunshot_sound': "assets/sounds/sniper_rifle/sniper_shot.wav", 'reload_sound': "assets/sounds/sniper_rifle/sniper_reload.wav"},
    'Dragunov':       {'bullet_speed': math.sqrt(80.0)*2, 'damage': 85,  'projectiles': 1, 'bullet_inaccuracy': 2.5,'firing_delay': 0.9, 'ammo_capacity': 10, 'reload_time': 0.91,  'penetration': 1, 'gunshot_sound': "assets/sounds/sniper_rifle/sniper_shot.wav", 'reload_sound': "assets/sounds/sniper_rifle/sniper_reload.wav"},
    'Barrett M82':    {'bullet_speed': math.sqrt(100.0)*2,'damage': 120, 'projectiles': 1, 'bullet_inaccuracy': 0.5,'firing_delay': 2.0, 'ammo_capacity': 10, 'reload_time': 0.91,  'penetration': 3, 'gunshot_sound': "assets/sounds/sniper_rifle/sniper_shot.wav", 'reload_sound': "assets/sounds/sniper_rifle/sniper_reload.wav"},
    'M24':            {'bullet_speed': math.sqrt(90.0)*2, 'damage': 95,  'projectiles': 1, 'bullet_inaccuracy': 1.5,'firing_delay': 1.4, 'ammo_capacity': 5,  'reload_time': 0.91,  'penetration': 2, 'gunshot_sound': "assets/sounds/sniper_rifle/sniper_shot.wav", 'reload_sound': "assets/sounds/sniper_rifle/sniper_reload.wav"},
    'Kar98k':         {'bullet_speed': math.sqrt(88.0)*2, 'damage': 90,  'projectiles': 1, 'bullet_inaccuracy': 2,  'firing_delay': 1.5, 'ammo_capacity': 5,  'reload_time': 0.91,  'penetration': 2, 'gunshot_sound': "assets/sounds/sniper_rifle/sniper_shot.wav", 'reload_sound': "assets/sounds/sniper_rifle/sniper_reload.wav"},
}


def new_equip(new_gun):
    settings.EQUIPPED = new_gun
    gun = gun_data[settings.EQUIPPED]
    settings.BULLET_SPEED = gun['bullet_speed']
    settings.BULLET_INACCURACY = gun['bullet_inaccuracy']
    settings.AMMO_CAPACITY = gun['ammo_capacity']
    settings.AMMO_COUNT = gun['ammo_capacity']
    settings.DAMAGE = gun['damage']
    settings.PENETRATION = gun['penetration']
    settings.GUNSHOT_SOUND = gun['gunshot_sound']
    sounds.update_gunshot_sound()
