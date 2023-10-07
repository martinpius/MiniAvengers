from typing import Final, List


Character = dict[str, str or int]
WIN_MSG: Final[str] = """
Hurray!! The avengers defeated Thanos, 
The planet is saved!!!
Every body is happy but for how long... Thanos must be regrouping for next inversion
 """
LOS_MSG: Final[str] = """
Thanos has killed all the avengers.......
The planet is whiped out of existence.....!!
"""

def getAllheroes()-> Character:
    """
    This module creates all super heroes and their characters
    """
    IRONMAN: Final[Character] = {"name": "IronMan", "Life": 400, "AttackPower": 900}
    SPIDERMAN: Final[Character] = {"name": "SpiderMAn", "Life": 150, "AttackPower": 240}
    BLACKWIDOW: Final[Character] = {"name": "BlackWidow", "Life": 130, "AttackPower": 210}
    CAPTAINAMERICA: Final[Character] = {"name": "SteveRogers", "Life": 450, "AttackPower": 1200}
    THOR: Final[Character] = {"name": "Thor", "Life": 1000, "AttackPower": 2000}
    HULK: Final[Character] = {"name": "Bunner", "Life": 800, "AttackPower": 1800}
    heroes: Character = [IRONMAN, SPIDERMAN, BLACKWIDOW,CAPTAINAMERICA,THOR, HULK]
    return heroes

def getAllVilains()->Character:
    """
    This module creates all super villains and their characters
    """
    REDSKULL: Final[Character] = {"name": "RedSkull", "Life": 560, "AttackPower": 1400}
    RENON: Final[Character] = {"name": "Renon", "Life": 800, "AttackPower": 1550}
    KANG: Final[Character] = {"name": "KangTheConqurer", "Life":1000, "AttackPower":2200}
    ZEUS: Final[Character] = {"name": "Zeuz", "Life": 1000, "AttackPower": 1900}
    THANOS: Final[Character] = {"name": "Thanos", "Life": 2500, "AttackPower": 3000}
    villains: Character = [REDSKULL, RENON, KANG, ZEUS, THANOS]
    return villains

def getHero(idx: int) -> Character or None:
    """
    This module fetch a hero at random from the list of all heroes
    """
    heroes = getAllheroes()
    if idx < len(heroes):
        return heroes[idx]
    else:
        return None
   
def getVillain(idx: int)-> Character or None:
    """
    This Module fetch a random Villain from the list of all villains
    """
    villains = getAllVilains()
    if idx < len(villains):
        return villains[idx]
    else: 
        return None
    



