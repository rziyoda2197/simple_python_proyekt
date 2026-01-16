import random


def play_game():
    secret = random.randint(1, 100)
    attempts = 0

    print("Men 1 dan 100 gacha son o‘yladim")

    while True:
        guess = input("Son kiriting (chiqish uchun q): ")

        if guess.lower() == 'q':
            print("O‘yin tugadi")
            break

        if not guess.isdigit():
            print("Iltimos, son kiriting")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Kattaroq son")
        elif guess > secret:
            print("Kichikroq son")
        else:
            print(f"Topdingiz! {attempts} urinishda")
            break


if __name__ == '__main__':
    play_game()
