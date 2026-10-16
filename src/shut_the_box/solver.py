from shut_the_box.game import remove_numbers, is_win, possible_moves

memo = {}

def dice_probability(value):
    dic_proba={2:1,3:2,4:3,5:4,6:5,7:6,8:5,9:4,10:3,11:2,12:1}
    return dic_proba[value]/36

def win_probability_unoptimized(remaining):

    if is_win(remaining):
        return 1
    
    best_prob=[]

    for dice_value in range(2,13):
        prob_win=0
        l = possible_moves(remaining,dice_value)
        best_prob_win = 0

        for i in l:
            new_remaining = remove_numbers(remaining,i)
            prob_win = win_probability_unoptimized(new_remaining)

            if prob_win>best_prob_win:
                best_prob_win = prob_win

        best_prob.append(best_prob_win* dice_probability(dice_value))

    return sum(best_prob)



def win_probability_optimized(remaining):
    state = tuple(sorted(remaining))

    if state in memo:
        return memo[state]
    
    if is_win(remaining):
        memo[state]=1
        return memo[state]
    
    best_prob=[]

    for dice_value in range(2,13):
        prob_win=0
        l = possible_moves(remaining,dice_value)
        best_prob_win = 0

        for i in l:
            new_remaining = remove_numbers(remaining,i)
            prob_win = win_probability_optimized(new_remaining)

            if prob_win>best_prob_win:
                best_prob_win = prob_win

        best_prob.append(best_prob_win* dice_probability(dice_value))
    memo[state] = sum(best_prob)
    return memo[state]

def best_choice(remaining,dice_value):
    win_probability_optimized(remaining)
    l = possible_moves(remaining,dice_value)
    best_proba=0
    best_move = {}
    for i in l:
        new_remaining = remove_numbers(remaining,i)
        if memo[tuple(sorted(new_remaining))]>best_proba:
            best_proba = memo[tuple(sorted(new_remaining))]
            best_move = i
    if len(best_move)==0:
        return "No move"
    return best_move

if __name__ == "__main__":
    print(f" The propabilityto win is : {win_probability_optimized({1,2,3,4,5,6,7,8,9,10,11,12}) *100}%")