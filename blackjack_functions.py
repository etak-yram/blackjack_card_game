
# check for blackjack
def blackjack_check(player_score, dealer_score):
    if player_score == 21 or dealer_score == 21:
        return True

# evaluate scores
def evaluate_final_scores(player_score, dealer_score):
    if (player_score == 21) or (dealer_score == 21):
        if player_score == 21:
            print('Game ends - Player Has Blackjack!\nPlayer Wins!')
        else:
            print('Game ends - Dealer Has Blackjack!\nDealer Wins!')

    elif (player_score > 21) or (dealer_score > 21):
        if player_score > 21:
            print('Game ends - Player Bust!\nDealer Wins!')
        else:
            print('Game ends - Dealer Bust!\nPlayer Wins!')

    else:
        if dealer_score < player_score < 21:
            print('Player Wins!')
        elif player_score < dealer_score < 21:
            print('Dealer Wins!')
        else:
            print('It looks like a draw...')
