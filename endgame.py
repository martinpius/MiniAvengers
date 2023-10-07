from attack import  exhaust_many_chances
from timeit import default_timer as timer


def mytimer(t: float = timer())->float:
    h = int(t / (60 * 60))
    m = int(t % (60 * 60) / 60)
    s = int(t % 60)
    return f"hrs: {h:02}, mins: {m:>02}, secs: {s:>02.5f}"

def main()->None:
    print(f" \n The battle has started, Lets hope for the best\
          \n {'*'*80}")
    t1 = timer()
    exhaust_many_chances(10)
    t2 = timer()
    print(f"\n>>>> The battle of the Titans has fought for the duration of {mytimer(t2 - t1)}")

main()