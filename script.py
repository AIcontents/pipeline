import random


def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            guess = int(input("Твоя догадка: "))
            attempts += 1

            if guess < number:
                print("Слишком мало! Попробуй ещё раз.")
            elif guess > number:
                print("Слишком много! Попробуй ещё раз.")
            else:
                print(f"Поздравляю! Ты угадал число {number} за {attempts} попыток!")
                break
        except ValueError:
            print("Пожалуйста, введи корректное число.")


if __name__ == "__main__":
    guess_number()
