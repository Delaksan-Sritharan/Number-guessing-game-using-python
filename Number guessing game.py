import random

def is_number(str):
    for char in str:
        if not('0'<=char<='9'):
            return False
        return True
def number_guessing_game():
    number=random.randint(1,100)
    attempts=0

    print("Welcome to Delaksan's Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")

    while True:
        guess_num=input("Guess a number= ")
        if is_number(guess_num):
            guess = int(guess_num)
            attempts+=1

            if guess <number:
                print("Too low!")
            elif guess>number:
                print("Too high!")
            else:
                print(f'Congrtulations! You guessed the number{number} in {attempts} attempts.')
                break

        else:
            print("Invalid input. Please re-enter a number.")


if __name__ == "__main__":
  number_guessing_game()



