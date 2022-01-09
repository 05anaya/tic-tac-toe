class Board(object):
    def __init__(self) -> None:
        self.cells = [" "," "," "," "," "," "," "," "," "] #  initializing the tiles on the board as space 

    # making the board which is diaplayed to the user
    def display(self):
        print(f"  {self.cells[0]}  |  {self.cells[1]}  |  {self.cells[2]} ")
        print("-----|-----|-----")
        print(f"  {self.cells[3]}  |  {self.cells[4]}  |  {self.cells[5]} ")
        print("-----|-----|-----")
        print(f"  {self.cells[6]}  |  {self.cells[7]}  |  {self.cells[8]} ")
        print("")

    # caluculating the the exact spot where user want to put their mark   
    def move(self, row, col, mark): 
        if row > 0 and row <= 3 and col > 0 and col <= 3:
            index = (row - 1)*3 + (col - 1)
            """ providing a validation where :
            if the tile is not space, " " then we are printing an error message and asking the user to input again """
            if self.cells[index] == " ":
                self.cells[index] = mark
            else:
                print("the place is already filled!")
                return False
            return True
        else:
            print("Invalid input!")
            return False
    
    # function for finding the winner
        # returning mark, or "-" for tie
    def result(self) -> str:
        if self.cells[0] == self.cells[1] and self.cells[0] == self.cells[2] and self.cells[0] != " ":
            return self.cells[0]
        elif self.cells[0] == self.cells[3] and self.cells[0] == self.cells[6] and self.cells[0] != " ":
            return self.cells[0]
        elif self.cells[0] == self.cells[4] and self.cells[0] == self.cells[8] and self.cells[0] != " ":
            return self.cells[0]
        elif self.cells[3] == self.cells[4] and self.cells[3] == self.cells[5] and self.cells[3] != " ":
            return self.cells[3]
        elif self.cells[6] == self.cells[7] and self.cells[6] == self.cells[8] and self.cells[6] != " ":
            return self.cells[6]
        elif self.cells[2] == self.cells[5] and self.cells[2] == self.cells[8] and self.cells[2] != " ":
            return self.cells[2]
        elif self.cells[2] == self.cells[4] and self.cells[2] == self.cells[6] and self.cells[2] != " ":
            return self.cells[2]
        elif self.cells[1] == self.cells[4] and self.cells[1] == self.cells[7] and self.cells[1] != " ":
            return self.cells[1]
        else: 
            draw = True
            for i in range(0,9):
                if self.cells[i] == " ":
                    return None
            return "-"

# asking the player, which is th user, to input the details
class Player(object):
    def __init__(self, name, mark) -> None:
        self.name = name
        self.mark = mark

    # asking the user for the input of the row and column
    def get_Position(self):
        print(f"{self.name}'s turn")
        row = int(input("Enter row -> ")) 
        col = int(input("Enter column -> "))
        return (row,col)

    # getting the user's name
    def get_name(self):
        return self.name

class Game(object):
    def __init__(self,p1,p2) -> None:
        self.b = Board()
        self.p1 = Player(p1, "X")
        self.p2 = Player(p2, "O")
        self.turn = 1
    
    def play(self):
        self.b.display()
        while self.b.result() == None: # continuing to play until their is a result 
            row, col = 0, 0 
            if self.turn == 1: 
                row, col = self.p1.get_Position()
                if self.b.move(row, col, self.p1.mark):
                    self.turn = 2  # flipping the turn
            else:
                row, col = self.p2.get_Position()
                if self.b.move(row, col, self.p2.mark):
                    self.turn = 1   # flipping the turn

            self.b.display()
        
        # displaying the winner or tie
        result = self.b.result()
        if result == self.p1.mark:
            print(f"The Winner is {self.p1.name}")
        elif result == self.p2.mark:
            print(f"The Winner is {self.p2.name} ")
        else:
            print("It is a Tie")

# asking user for input of the names
p1_name = input("enter the name of the 1st player : ")
p2_name = input("enter the name of the 2nd player : ")

# calling the class game
g = Game(p1_name, p2_name)
g.play()