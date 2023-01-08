from blackjack_classes import Deck, Hand


def play():
    # initiate scores
    dealer_score = 0
    player_score = 0

    print('////// Welcome to Blackjack! //////\n')

    # create and deck
    deck = Deck()
    deck.shuffle_deck()

    # deal initial cards for dealer

    dealer_hand = Hand('Dealer Hand')
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    print('Dealers Hand: ||   ??   ||   ??   ||\n')

    dealer_hand.add_score()
    dealer_score += dealer_hand.score

    # deal player cards

    player_hand = Hand('Your Hand: ')
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    print(player_hand)
    player_hand.add_score()
    player_score += player_hand.score
    player_hand.show_score()

    # assess player score

    if player_score > 21:
        print('Player is Bust!')

    if player_score == 21:
        print('Blackjack, Player Wins!')

    while player_score <= 21:
        next_move = input('Stand or Hit?: ')

        if next_move == 'Hit':
            player_hand.add_card(deck.deal_card())
            player_hand.add_score()
            continue
        if next_move == 'Stand':
            print('Player Stands!\n')
            break


    if player_score > dealer_score:
        print('Player Wins!')
    else:
        print('Dealer Wins!')

    print('')
    print('---------------------------')


if __name__ == '__main__':
    play()
