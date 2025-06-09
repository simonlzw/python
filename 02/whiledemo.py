#石头剪刀布优化
import random
all_choice = ["Rock","Scissor","Paper"]
win_list = [["Rock","Scissor"],["Paper","Rock"],["Scissor","Paper"]]
cwin = 0
pwin = 0
while cwin < 2 and pwin < 2 :
    computer = random.choice(all_choice)
    player = input("Rock,Scissor,Paper:")
    print("Your choice:" + player)
    print("Computer choice:" + computer)
    if player == computer :
        print("Draw!")
    elif [player,computer] in win_list :
        print("You Win!")
        pwin += 1
    else :
        print("You Lose!")
        cwin += 1