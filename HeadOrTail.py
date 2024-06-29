import random

print(f"Tossing a coin...")
coinHit = [0, 0]
for i in range(3):
    print(f"Round {i}: ", end="")
    ans = random.randrange(0, 2)
    coinHit[ ans ] += 1
    if ans == 0:
        print(f"Heads")
    else:
        print(f"Tails")
print(f"Heads: {coinHit[ 0 ]}, Tails: {coinHit[ 1 ]}")