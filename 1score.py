score1 = int(input ("enter the value for score 1 "))
score2 = int(input ("enter the value for score 2 "))
score3 = int(input ("enter the value for score 3 "))
score4 = int(input ("enter the value for score 4 "))
score5 = int(input ("enter the value for score 5 "))
all=(score1,score2,score3,score4, score5)
higest=max(all)
lowest=min(all)
print(f"the highest score out of {score1}, {score2}, {score3}, {score4}, {score5}  = {higest}")
print(f"the lowest score out of {score1}, {score2}, {score3}, {score4}, {score5}  = {lowest}")
