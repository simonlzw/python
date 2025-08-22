import random

def exam():
    nums = [random.randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    tmp = random.choice("+-")
    if tmp == "+":
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]
    answer = int(input("%s %s %s = ?? Please Answer : " % (nums[0],tmp,nums[1])))
    if answer == result:
        print("You are right!")
    else:
        print("You are wrong!")

def menu():
    while True:
        exam()
        tmp = input("Exit(n/N): ")
        if  tmp in "nN" :
            print("Bye")
            break


if __name__ == "__main__" :
    menu()