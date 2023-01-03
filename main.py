def showBoard(xPart,yPart):
    Zero = 'X' if xPart[0] else ('O' if yPart[0] else 0)
    One = 'X' if xPart[1] else ('O' if yPart[1] else 1)
    Two = 'X' if xPart[2] else ('O' if yPart[2] else 2)
    Three = 'X' if xPart[3] else ('O' if yPart[3] else 3)
    Four = 'X' if xPart[4] else ('O' if yPart[4] else 4)
    Five = 'X' if xPart[5] else ('O' if yPart[5] else 5)
    Six = 'X' if xPart[6] else ('O' if yPart[6] else 6)
    Seven = 'X' if xPart[7] else ('O' if yPart[7] else 7)
    Eight = 'X' if xPart[8] else ('O' if yPart[8] else 8)
    print(f"{Zero} | {One} | {Two}")
    print(f"--|---|---")
    print(f"{Three} | {Four} | {Five}")
    print(f"--|---|---")
    print(f"{Six} | {Seven} | {Eight}")

def sum(a,b,c):
    return a+b+c

def winCheck(xPart,yPart):
    Wins = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
    for win in Wins:
        if sum(xPart[win[0]],xPart[win[1]],xPart[win[2]],) == 3:
            print("X wins!")
            return 1
        if sum(yPart[win[0]],yPart[win[1]],yPart[win[2]],) == 3:
            print("O wins!")
            return 0
    return -1

xPart = [0,0,0,0,0,0,0,0,0]
yPart = [0,0,0,0,0,0,0,0,0]

chance = 1    # 1 for X and 0 for O

print("TIC-TAC-TOE")
while True:
    showBoard(xPart,yPart)
    if chance == 1:
        print("It is X's chance")
        move = input("Enter a number position: ")
        x = move.isnumeric()
        if x == True:
            move = int(move)
            xPart[move] = 1
        else:
            print("Invalid Input | Chance Lost")
    else:
        print("It is Y's chance")
        move = input("Enter a number position: ")
        y = move.isnumeric()
        if y == True:
            move = int(move)
            yPart[move] = 1
        else:
            print("Invalid Input | Chance Lost")
        yPart[move] = 1
    check = winCheck(xPart,yPart)
    if check != -1:
        break
    chance = 1 - chance    