import random
from data.cards_list import card_list
from utils.numbers_sum import numbers_sum
from steps.start import start

blackjack = 21

user_numbers = [random.choice(card_list), random.choice(card_list)]
computer_numbers = [random.choice(card_list), random.choice(card_list)]

user_score = numbers_sum(user_numbers)
computer_score = numbers_sum(computer_numbers)

start(user_numbers, user_score, computer_numbers)
