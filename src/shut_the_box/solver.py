from game import remove_numbers, is_win, play_turn, NoPossibleMoveError, dice_probability, possible_moves


def win_probability(remaining):

    if is_win(remaining):
        return 1
    
    best_prob=[]

    for dice_value in range(2,13):
        prob_win=0
        l = possible_moves(remaining,dice_value)
        best_prob_win = 0

        for i in l:
            new_remaining = remove_numbers(remaining,i)
            prob_win = win_probability(new_remaining)

            if prob_win>best_prob_win:
                best_prob_win = prob_win

        best_prob.append(best_prob_win* dice_probability(dice_value))

    return sum(best_prob)


print(win_probability({1,2,3,4,5,6,7,8,9}))