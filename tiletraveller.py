UserInput = 0
x = 1
y = 1
strN = '(N)orth'
strS = '(S)outh'
strW = '(W)est'
strE = '(E)ast'
str1 = 'You can travel: {}.'
str2 = 'You can travel: {} or {}.'
str3 = 'You can travel: {} or {} or {}.'

def door(col,row):
    if x == 1 and y == 1 or x == 2 and y == 1:
        print(str1.format(strN))
        global direction
        direction = 'N'
    
    elif x == 1 and y == 2:
        print(str3.format(strN,strE,strS))
        direction = 'NES'
    elif x == 1 and y == 3:
        print(str2.format(strE,strS))
        direction = 'ES'

    elif x == 2 and y == 2:
        print(str2.format(strS,strW))
        direction = 'SW'

    elif x == 2 and y == 3:
        print(str2.format(strE,strW))
        direction = 'EW'

    elif x == 3 and y == 2:
        print(str2.format(strN,strS))
        direction = 'NS'

    elif x == 3 and y == 3:
        print(str2.format(strS,strW))
        direction = 'SW'

def att():
    global x
    global y
    dirInput = input('Direction: ')
    dirInput = dirInput.upper()
    if dirInput not in direction:
        print('Not a valid direction!')
    elif dirInput in direction and dirInput == 'N':
        y += 1
    elif dirInput in direction and dirInput == 'S':
        y += -1
    elif dirInput in direction and dirInput == 'E':
        x += 1
    elif dirInput in direction and dirInput == 'W':
        x += -1

while True:
    door(x,y)
    att()

    if x == 3 and y ==  1:
        break

print('Victory!')