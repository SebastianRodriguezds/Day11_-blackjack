from logo import logo
import random

print(logo)

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score caculated from the cards"""
  if len(cards) == 2 and sum(cards) == 21:
    return 0
  elif 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(u_score , c_score):
  """Compare the scores to """
  if u_score == c_score:
    return "Is a draw"
  elif c_score == 0:
    return "Lose, opponent has Blackjack"
  elif u_score == 0:
    return "Win, with a Blackjack"
  elif u_score > 21:
    return "You when over, you lose"
  elif c_score > 21:
    return "Opponent when over. You win"
  elif c_score > u_score:
    return "You lose"
  else:
    return "You win"
  
def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  computer_score = -1
  user_score = -1
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  print(user_cards)
  print(computer_cards)

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      answer = input(str("Would you like to draw another card? if yes type 'y' if not 'n': ").lower())
    if answer == "y":
      user_cards.append(deal_card())
      print(f"a new card added : {user_cards}")
    else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


  print(f"Your final hand: {user_cards} and your final score: {user_score}")
  print(f"Computer final hand: {computer_cards} and final score: {computer_score}")
  print(compare(user_score, computer_score))


while input(f"Do you want to play a game of Blackjack? if yes press 'y' if no press 'n'") == 'y':
  print("\n"*100)
  play_game()
