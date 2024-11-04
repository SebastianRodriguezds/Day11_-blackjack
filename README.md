############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################# Requirements ################################

# Deal both user and computer a starting hand of 2 random card values.
# Detect when computer or user has a blackjack. (Ace + 10 value card).
# If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack, then they win (unless the computer also has a blackjack).
# Calculate the user's and computer's scores based on their card values.
# If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
# Reveal computer's first card to the user.
# Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
# Ask the user if they want to get another card.
# Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.
# Compare user and computer scores and see if it's a win, loss, or draw.
# Print out the player's and computer's final hand and their scores at the end of the game.

###############################################################