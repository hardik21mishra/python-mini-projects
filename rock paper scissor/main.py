import random

class InvalidInputError(Exception):
    pass
'''
# below is the more optimised way of writing the function winner
def winner(inp, pcchoice):
    if inp == pcchoice:
        return "It's a tie!"
    elif (inp == 'rock' and pcchoice == 'scissor') or \
         (inp == 'paper' and pcchoice == 'rock') or \
         (inp == 'scissor' and pcchoice == 'paper'):
        return "You won!!! Congratulations!"
    else:
        return "Computer wins!"
'''
def winner(inp, pcchoice):
    if inp == 'rock':
        if pcchoice ==  'rock':
            return "It's a tie"
        elif pcchoice == 'paper':
            return "computer wins"
        elif pcchoice == 'scissor':
            return "you won!!! Congratulations"
        
    elif inp == 'paper':
        if pcchoice ==  'rock':
            return "you won!!! Congratulations"
        elif pcchoice == 'paper':
            return "It's a tie"
        elif pcchoice == 'scissor':
            return "computer wins"
        
    elif inp == 'scissor':
        if pcchoice ==  'rock':
            return "computer wins"
        elif pcchoice == 'paper':
            return "you won!!! Congratulations"
        elif pcchoice == 'scissor':
            return "It's a tie"

def play_game():
    count = 0
    pc_score = 0
    user_score = 0
    while(True):
        
        inp = input("choose rock, paper, scissor or quit ---> ")
        if inp not in ['rock', 'paper', 'scissor', 'quit']:
            print('Invalid Input')
            continue
        
        
        if inp == 'quit':
            print("----------------GAME OVER--------------------")
            break
        try:
            para = ['rock', 'paper', 'scissor']
            pcchoice = random.choice(para)
            print(f'PC chooses {pcchoice}')

            result = winner(inp, pcchoice)
            print(result)
            count += 1


            if "you won!!! Congratulations" in result:
                user_score += 1
            elif "computer wins" in result:
                pc_score += 1

            print(f'Total chances played ---> {count}')
            print(f'Your score ---> {user_score}')
            print(f'PC score ---> {pc_score}')
        except InvalidInputError as e:
            print(e)

        print('\n')
        
if __name__ == "__main__":
    play_game()