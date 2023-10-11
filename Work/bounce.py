# bounce.py
#
# Exercise 1.5

def main():
    height = 100
    bouncesLeft = 1
    while bouncesLeft <= 10:
        height = height * 3 / 5
        print(bouncesLeft, round(height, 4))
        bouncesLeft += 1

main()
