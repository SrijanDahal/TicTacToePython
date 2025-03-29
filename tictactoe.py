tictactoe = [
    ["", "", ""],
    ["", "", ""], 
    ["", "", ""]]

print("Player1 is always X and Player2 is always Y.")

# Making a function to check the winning 

def checking():
    if((tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X")
       or (tictactoe[1][0] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X")
       or (tictactoe[2][0] == "X" and tictactoe[2][1] == "X" and tictactoe[2][2] == "X")
       or (tictactoe[0][0] == "X" and tictactoe[1][0] == "X" and tictactoe[2][0] == "X")
       or (tictactoe[0][1] == "X" and tictactoe[1][1] == "X" and tictactoe[2][1] == "X")
       or (tictactoe[0][2] == "X" and tictactoe[1][2] == "X" and tictactoe[2][2] == "X")
       or (tictactoe[0][0] == "X" and tictactoe[1][1] == "X" and tictactoe[2][2] == "X")
       or (tictactoe[0][2] == "X" and tictactoe[1][1] == "X" and tictactoe[2][0] == "X")):
        
        return "X won"
    
    elif ((tictactoe[0][0] == "O" and tictactoe[0][1] == "O" and tictactoe[0][2] == "O")
       or (tictactoe[1][0] == "O" and tictactoe[1][1] == "O" and tictactoe[1][2] == "O")
       or (tictactoe[2][0] == "O" and tictactoe[2][1] == "O" and tictactoe[2][2] == "O")
       or (tictactoe[0][0] == "O" and tictactoe[1][0] == "O" and tictactoe[2][0] == "O")
       or (tictactoe[0][1] == "O" and tictactoe[1][1] == "O" and tictactoe[2][1] == "O")
       or (tictactoe[0][2] == "O" and tictactoe[1][2] == "O" and tictactoe[2][2] == "O")
       or (tictactoe[0][0] == "O" and tictactoe[1][1] == "O" and tictactoe[2][2] == "O")
       or (tictactoe[0][2] == "O" and tictactoe[1][1] == "O" and tictactoe[2][0] == "O")):
        
        return "O won"

    else: 
        return False



def logic():
    turn = 0
    while(turn < 8): 
    # Taking user inputs
        userrow1 = int(input("\nPlayer1! Enter a row number(0, 1 or 2): "))
        usercol1 = int(input("Player1! Enter a column number(0, 1 or 2): "))
        
        
        userrow2 = int(input("\nPlayer2! Enter a row number(0, 1 or 2): "))
        usercol2 = int(input("Player2! Enter a column number(0, 1 or 2): "))
        
        # Checking if the spot is empty or not
        if(tictactoe[userrow1][usercol1] != "" or tictactoe[userrow2][usercol2] != ""):
            print("\nPlease make sure the cell is not empty or make sure you play in the field that is not played already.")
        
        # Placing the marks
        else: 
            if(tictactoe[userrow1][usercol1] == ""):
                tictactoe[userrow1][usercol1] = "X"
            
            if (tictactoe[userrow2][usercol2] == ""):  
                tictactoe[userrow2][usercol2] = "O"
        
        turn = turn + 2
        print(tictactoe)
        
        result = checking()
        print(turn)
        
        if(result):
            return result

    else:
        return "Draw"
    

print(f"\n {logic()}")
    
    