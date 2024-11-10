import random
from data.cards_list import card_list
from utils.numbers_sum import numbers_sum
from data.art import art

blackjack = 21

def start(user_numbers,user_score, computer_numbers):
    print(art)
    print(f"Your current numbers is {user_numbers} - Current score is: {user_score}\n")
    print(f"The computer first number is {computer_numbers[0]}")


def adjust_ace(cards):
    while cards.count(11) > 0 and numbers_sum(cards) > blackjack:
        cards[cards.index(11)] = 1
    return cards

def play_round():

    user_numbers = [random.choice(card_list), random.choice(card_list)]
    computer_numbers = [random.choice(card_list), random.choice(card_list)]


    user_numbers = adjust_ace(user_numbers)
    computer_numbers = adjust_ace(computer_numbers)

    user_score = numbers_sum(user_numbers)
    computer_score = numbers_sum(computer_numbers)

    start(user_numbers, user_score, computer_numbers)

    while True:
        answer = input("Do you want another card? (y/n) ").lower()

        if answer == "y":

            number = random.choice(card_list)
            user_numbers.append(number)
            user_numbers = adjust_ace(user_numbers)

            user_score = numbers_sum(user_numbers)
            print(f"Your numbers are {user_numbers} - Your score is: {user_score}")

            if user_score > blackjack:
                print(f"You are Fired! Computer's numbers were {computer_numbers}, score = {computer_score}")
                return user_score, computer_score, False
        elif answer == "n":

            print(f"Final scores - Your: {user_numbers} = {user_score}, Computer: {computer_numbers} = {computer_score}")

            if user_score == blackjack and computer_score == blackjack:
                print("It's a tie! Both have BlackJack!")
                return user_score, computer_score, None
            elif user_score == blackjack:
                print("You has the BlackJack!")
                return user_score, computer_score, True
            elif computer_score == blackjack:
                print("Computer has the BlackJack!")
                return user_score, computer_score, False
            elif user_score == computer_score:
                print("It's a tie!")
                return user_score, computer_score, None
            elif user_score > computer_score and user_score <= blackjack:
                return user_score, computer_score, True
            else:
                print("Computer wins!")
                return user_score, computer_score, False
        else:
            print("Please enter 'y' or 'n'.")

def main():
    while True:

        user_score, computer_score, winner = play_round()

        if winner is None:
            print("It's a tie!")
        elif winner:
            print("You wins!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

main()
