# calculating score for higest and lowest
val1 = int(input ("enter the value for score 1: "))
val2 = int(input ("enter the value for score 2: "))
val3 = int(input ("enter the value for score 3: "))
if val1 >= val2 and val1 >= val3:
    print(f"The highest value is {val1}")
elif val2 > val1 and val2 > val3:
    print(f"The highest value is {val2}")
else:
    print(f"The highest value is {val3}")
