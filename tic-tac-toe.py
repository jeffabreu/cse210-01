#Author: Jefferson Abreu
#Assgnment: Tic-tac-toe
def main():
    numbertable = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    board = makeatable(numbertable[0], numbertable[1],numbertable[2],numbertable[3],numbertable[4],numbertable[5], numbertable[6],numbertable[7],numbertable[8])
    print (board)
    while not winner(numbertable[0], numbertable[1], numbertable[2], numbertable[3], numbertable[4], numbertable[5], numbertable[6], numbertable[7], numbertable[8]):
        player1=int(input(f"x's turn to choose a square (1-9): "))
        numbertable[player1-1]="x"
        board = makeatable(numbertable[0], numbertable[1],numbertable[2],numbertable[3],numbertable[4],numbertable[5], numbertable[6],numbertable[7],numbertable[8])
        print (board)
        player2=int(input(f"o's turn to choose a square (1-9): "))
        numbertable[player2-1]="o"
        board = makeatable(numbertable[0], numbertable[1],numbertable[2],numbertable[3],numbertable[4],numbertable[5], numbertable[6],numbertable[7],numbertable[8])
        print (board)
    print("Good game. Thanks for playing!")
        

def winner(first, second, third, fourth, fifth, sixth, seventh, eighth, nineth):
    return (first == second == third or
            fourth == fifth == sixth or
            seventh == eighth == nineth or
            first == fifth == nineth or
            third == fifth == seventh or
            first == fourth == seventh or
            second == fifth == eighth or
            third == sixth == nineth)
def makeatable(one, two, three, four,five, six, seven, eight, nine):
    table = one +"|" + two+"|"+three+"\n"+four+"|"+five+"|"+six+"\n"+ seven+"|"+eight+"|"+nine
    return table

if __name__ == "__main__":
    main()