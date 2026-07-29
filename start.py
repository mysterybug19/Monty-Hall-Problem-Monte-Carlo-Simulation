import random

#monte carlo simulation
doors=[1,2,3]
stay_wins = 0
switch_wins = 0
N=int(input())

for i in range (N):
    car = random.choice(doors)
    player = random.choice(doors)
    possible = [d for d in doors if d != player and d != car]
    host = random.choice(possible)
    switch = [d for d in doors if d != player and d != host][0]
    if player == car:
        stay_wins += 1

    if switch == car:
        switch_wins += 1

print("Stay win rate:", stay_wins / N)
print("Switch win rate:", switch_wins / N)