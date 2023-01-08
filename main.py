from blackjack_classes import Deck, Hand, blackjack_check



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

    # deal initial cards for player

    player_hand = Hand('Your Hand: ')
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    print(player_hand)
    player_hand.add_score()
    player_hand.show_score()


    # blackjack check

    blackjack_check(dealer_score)
    blackjack_check(player_score)

    # decide next moves

    if dealer_score > 21:
        print('Dealer Bust, Player Wins!')
    elif dealer_score >= 17:
        print('Dealer Stands')
    elif dealer_score < 17:
        print('Dealer Hits!')
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_score()

    if player_score > 21:
        print('Player Bust, Dealer Wins!')
    elif player_score == 21:
        print('Blackjack, Player Wins!')
    else:
        next_move = input('Stand or Hit?: ')
        if next_move == 'Hit':
            player_hand.add_card(deck.deal_card())
            player_hand.add_score()
            player_hand.show_score()
        if next_move == 'Stand':
            print('Player Stands!\n')
            if dealer_score > player_score:
                print('Dealer Wins!')
                print('Dealer Score: {}'.format(dealer_score))
            elif dealer_score == player_score:
                print('Game is Drawn!')
            else:
                print('Player Wins!')


    print('')
    print('---------------------------')

if __name__ == '__main__':
    play()
