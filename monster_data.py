#Enemy Locations
enemyList = {
    'Green Field': ['greenSlime', 'greenSlime', 'bat', 'bat', 'zombie'],
    'greenSlime': {
        'name': 'Green Slime',
        'hp': 5,
        'damage_min': 1,
        'damage_max': 2,
        'defense': 0,
        'money_min': 1,
        'money_max': 4,
        'exp_min': 1,
        'exp_max': 3,
        'item_drop': ['small_health_pot', 'small_mp_pot']
        },
    'bat': {
        'name': 'Bat',
        'hp': 3,
        'damage_min': 1,
        'damage_max': 2,
        'defense': 0,
        'money_min': 1,
        'money_max': 2,
        'exp_min': 1,
        'exp_max': 2,
        'item_drop': ['small_health_pot', 'small_mp_pot']
        },
    'zombie': {
        'name': 'Zombie',
        'hp': 8,
        'damage_min': 2,
        'damage_max' : 3,
        'defense': 0,
        'money_min': 2,
        'money_max': 6,
        'exp_min': 2,
        'exp_max': 4,
        'item_drop': ['small_health_pot', 'small_mp_pot']
        }
    }