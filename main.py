# init the majong to '0'
dict = {}

limit_up = 0
limit_down = 24
limit_left = 0
limit_right = 4
for i in range(25):

    up = -1
    down = -1
    left = -1
    right = -1
    # check the limit to go upside
    if i - 5 >= limit_up:
        up = i - 5
    
    # check the limit to go downside
    if i + 5 <= limit_down:
        down = i + 5
    # check the limit to go rightside
    if i + 1 <= limit_right:
        right = i + 1
    else:
        limit_right += 5
    # check the limit to go leftside
    if i == 0:
        left = -1
    elif (i + 1) % 5 == 0:
        limit_left += 5
        left = i - 1
    elif i - 1 >= limit_left:
        left = i - 1


    dict[i] = {"value": 0, "up": up, "down": down, "left": left, "right": right}

print "### STAGE - 0 - ###\n"
line = ""
for i in range(25):
    line += str(dict[i]["value"]) + " "
    if (i + 1) % 5 == 0:
        print line
        line = ""
    
    
    
