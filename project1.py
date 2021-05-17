def drawField(field):
    for row in range(11):
        if row%2 == 0:
            prRow = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    prColumn = int(column/2)
                    if column != 12:
                        print(field[prColumn][prRow], end="")
                    else:
                        print(field[prColumn][prRow])
                else:
                    print("|", end="")    
        else:
            print("-------------")


Player = 1
currentField = [[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "]]
drawField(currentField)
while(True):
    print("Players turn: ",Player)
    MoveColumn = int(input("Please select a column: "))
    MoveRow = -1
    if Player == 1:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            MoveRow -= 1
        else:
            MoveRow -= 1
            currentField[MoveColumn][MoveRow] = "X"
            MoveRow -= 1
        Player = 2
    else:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            MoveRow -= 1
        else:
            MoveRow -= 1
            currentField[MoveColumn][MoveRow] = "O"
            MoveRow -= 1
        Player = 1
    drawField(currentField)