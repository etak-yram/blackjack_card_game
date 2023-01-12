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

    dealer_hand.show_dealer_hand()

    # deal players hand
    player_hand = Hand('Players ')
    for deal in range(2):
        player_hand.add_card(deck.deal_card())
        player_hand.add_score()

    # output player hand
    print(player_hand.deck)
    player_hand.show_score()

    while dealer_hand.score < 21 and player_hand.score < 21:

        if dealer_hand.score == 21 or player_hand.score == 21:
            break

        if dealer_hand.score < 17:
            print('\nDealer Hits!\n')
            dealer_hand.add_card(deck.deal_card())
            dealer_hand.add_score()
            dealer_hand.show_score()
            if dealer_hand.score > 21:
                print('Dealer Bust!')
                break

        next_move = input('Player: Hit or Stand?')
        if next_move == 'Hit':
            player_hand.add_card(deck.deal_card())
            player_hand.add_score()
            print(player_hand.deck)
            player_hand.show_score()
            if player_hand.score > 21:
                print('Player Bust!')
                break
        elif next_move == 'Stand':
            print('Player Stands!')
            break
        continue

    print('\nChecking Scores...\n')

    if (player_hand.score == 21) or (dealer_hand.score == 21):
        if player_hand.score == 21:
            print('Game ends - Player Has Blackjack!')
            player_hand.show_score()
            dealer_hand.show_score()
        else:
            print('Game ends - Dealer Has Blackjack!')
            player_hand.show_score()
            dealer_hand.show_score()
    elif (player_hand.score > 21) or (dealer_hand.score > 21):
        if player_hand.score > 21:
            print('Game ends - Player Bust!')
            player_hand.show_score()
            dealer_hand.show_score()
        else:
            print('Game ends - Dealer Bust!')
            player_hand.show_score()
            dealer_hand.show_score()
    else:
        if dealer_hand.score < player_hand.score < 21:
            print('Player Wins!')
            player_hand.show_score()
            dealer_hand.show_score()
        elif player_hand.score < dealer_hand.score < 21:
            print('Dealer Wins!')
            dealer_hand.show_score()
            player_hand.show_score()
        else:
            print('It looks like a draw...')
            dealer_hand.show_score()
            player_hand.show_score()


if __name__ == '__main__':
    play()
