# Part One
pass_count = 0
total_score = 0
for num in  range(1,5):
    score = float(input(f"Score {num}: "))

    if score >= 60 :
        pass_count += 1
        total_score += score
        print("Pass")
    elif score < 0:
        print("Try Again")
    else:
        total_score += score
        print("Try Again")
    

avg_score = total_score / 4

print("Passing Count: ", pass_count)
print("Average Score: ", avg_score)


# Part Two
saving_goal = int(input("Savings goal:"))

saved_money = 0
count = 0
while True:
    deposit = int(input("Deposit: "))
    if deposit > 0:
        count += 1
        saved_money += deposit
        print("Saved so far: ", saved_money)
    else:
        print("Invalid deposit")
    
    if saved_money >= saving_goal:
        print("Goal Reached! ")
        print("Savings goal: ", saving_goal)
        print("Final saved total: ", saved_money)
        print("Accepted deposit: ", deposit)
        above_goal = saved_money - saving_goal
        print("Above goal: ", above_goal)
        break

