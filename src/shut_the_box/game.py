import random

class NoPossibleMoveError(Exception):
    pass


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

def roll_dice():
    d1 = random.randint(1,6)
    d2=random.randint(1,6)
    return d1+d2

def play_turn(remaining):

    flag_choice=True
    result = roll_dice()
    l = possible_moves(remaining,result)

    if len(l)==0:
        raise NoPossibleMoveError("No possible move")

    for i in range(len(l)):
        print(f"Choice {i} : {l[i]}\n")

    while(flag_choice):
        choice = int(input("Enter your choice\n"))
        if choice<0 or choice>=len(l):
            print("Invalide choice\n")
        else:
            flag_choice=False

    return remove_numbers(remaining,l[choice])

def play_game():

    remaining={1,2,3,4,5,6,7,8,9,10,11,12}

    while not is_win(remaining):
        try:
            remaining = play_turn(remaining)  
        except NoPossibleMoveError:
            print("\n You lose, there is no combination possible \n") 
            return 
        
    print("\n You won !! \n")    
    return 


play_game()