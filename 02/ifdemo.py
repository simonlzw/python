# if 0 :
#     print("0为false")
# else :
#     print("值为0")
#
# if ' ':
#     print('空格也是一个字符，为True')
#
# if [False]:
#     print('非空列表，为真True')
#
# if not None:
#     print('None为假，取反为真')

# 剪刀石头布小游戏
import random
all_choice = ["Rock","Scissor","Paper"]
win_list = [["Rock","Scissor"],["Paper","Rock"],["Scissor","Paper"]]
computer = random.choice(all_choice)
player = input("Rock,Scissor,Paper:")
print("Your choice:" + player)
print("Computer choice:" + computer)
if player == computer :
    print("Draw!")
elif [player,computer] in win_list :
    print("You Win!")
else :
    print("You Lose!")



