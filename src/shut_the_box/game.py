def remove_numbers(remaining,choice):
    new_remaining = remaining.copy()
    for number in choice:
        if number in new_remaining:
            new_remaining.remove(number)
    return new_remaining

def is_win(remaining):
    return len(remaining)==0

def possible_moves(remaining,target,current_choice = None):
    if current_choice is None:
        current_choice = set()

    total = sum(current_choice)

    if total==target:
        return [current_choice]
    
    if total>target or len(remaining)==0:
        return []

    new_remaining = remaining.copy()
    next_value = sorted(new_remaining)[0]
    new_remaining.remove(next_value)

    left_current_choice = current_choice.copy()
    left_current_choice.add(next_value)
    right_current_choice = current_choice.copy()

    left_result = possible_moves(new_remaining,target,left_current_choice)
    right_result = possible_moves(new_remaining,target,right_current_choice)

    return left_result + right_result


remaining={1,2,3,4,5,6,7,8,9,10,11,12}

print(possible_moves({1,2,3,4,7},7))