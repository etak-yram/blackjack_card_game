from blackjack_functions import *
from blackjack_classes import Deck, Hand



def play():
    print('Welcome to Blackjack!\n')

    # set up and shuffle deck
    deck = Deck()

    # deal dealers hand
    dealer_hand = Hand('Dealers ')
    for deal in range(2):
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_score()

    # show 'dealers hand' - only first card
    dealer_hand.show_dealer_hand()

    # deal players hand
    player_hand = Hand('Players ')
    for deal in range(2):
        player_hand.add_card(deck.deal_card())
        player_hand.add_score()

    # output player hand
    print(player_hand.deck)
    player_hand.show_score()


    # implement the game loop to run whilst player and dealer scores are under 21

    while dealer_hand.score < 21 and player_hand.score < 21:

        # first check for blackjack, if so break
        if dealer_hand.score == 21 or player_hand.score == 21:
            break

        # check dealer score and hit a card if it's under 17
        if dealer_hand.score < 17:
            print('\nDealer Hits!\n')
            dealer_hand.add_card(deck.deal_card())
            dealer_hand.add_score()
            dealer_hand.show_score()

            # check if dealer is bust, if so break
            if dealer_hand.score > 21:
                print('Dealer Bust!')
                break

        # implement a variable to prompt player for next move hit/stand
        next_move = input('Player: Hit or Stand?')

        # if hit is selected add card to hand and update score, print out new hand
        if next_move == 'Hit':
            player_hand.add_card(deck.deal_card())
            player_hand.add_score()
            print(player_hand.deck)
            player_hand.show_score()

            # check if player is bust, if so, break
            if player_hand.score > 21:
                print('Player Bust!')
                break

        # if stand is selected, break out the while loop
        elif next_move == 'Stand':
            print('Player Stands!')
            break

        # if no break conditions satisfied, loop around again
        continue


    # if loop is broken, message print to adv scores are being checked
    print('\nChecking Scores...\n')

    # check final scores
    evaluate_final_scores(player_hand.score, dealer_hand.score)

    # show final scores
    player_hand.show_score()
    dealer_hand.show_score()


    play_again = input('\nWould you like to play again? Y/N: ')
    if play_again == 'Y':
        play()
    else:
        print('\nThanks for playing!')


if __name__ == '__main__':
    play()
