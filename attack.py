from game_intro import getHero, getVillain, WIN_MSG, LOS_MSG
from random import randint

def heros_life_Increment(hero)->int:
    heros_life = hero["Life"]
    life = 0
    heros_life+=life
    return heros_life

def heros_life_Decrement(hero)->int:
    heros_life = hero["Life"]
    life = 0
    heros_life -= life
    return heros_life

def villain_life_Increment(villain)->int:
    villain_life = villain["Life"]
    life = 0
    villain_life += life
    return villain_life

def villain_life_Decrement(villain)->int:
    villain_life = villain["Life"]
    life = 0
    villain_life -= life
    return villain_life


def battle_of_the_Titans()-> str:
    for attack in range(3):

        h_idx = randint(0, 5)
        v_idx = randint(0, 4)
        hero = getHero(h_idx)
        villain = getVillain(v_idx)
        heros_life = heros_life_Increment(hero)
        villain_life = villain_life_Increment(villain)
        print(f"\n >>>> Attack: {attack + 1}, {hero['name']} is battling with {villain['name']}\n")

        heros_life -= villain['AttackPower']
        villain_life -= hero['AttackPower']
    if heros_life >= villain_life:
        print(f'{"*"*80}\n')
        print(WIN_MSG)
        
    else:
        print(f'{"*"*80}\n')
        print(LOS_MSG)
        

def exhaust_many_chances(chances: int)-> None:
    for _ in range(chances):

        battle_of_the_Titans()
        print(f"\n>>>> Game over!!!!! next trial begins, Someone is regrouping realy fast\n {'*'*80}")

if __name__ == "__main__":
    exhaust_many_chances(10)

    