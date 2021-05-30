#TIC TAC TOE IN PYTHON!
myboard = {'1' : ' ' , '2' : ' ' , '3' : ' ' ,
           '4' : ' ' , '5' : ' ' , '6' : ' ' ,
           '7' : ' ' , '8' : ' ' , '9' : ' '}

myboardkeys = []

for key in myboard:
    myboardkeys.append(key)

def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("-+-+-")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

    
def mygame():
    turn = 'X'
    count=0

    for i in range(10):
        print_board(myboard)
        print(turn + " its your turn.Please enter your next move.")

        move = input()

        if myboard[move]==' ':
            myboard[move]=turn
            count=count+1
        else:
            print("this place is already filled.Select some other place")
            continue 


        if count>=5:
            if myboard['1']==myboard['2']==myboard['3']!=' ':
                print_board(myboard)
                print(turn + " is the winner!!")
                print("*game over*")
                break
            elif myboard['4']==myboard['5']==myboard['6']!=' ':
                print_board(myboard)
                print(turn + " is the winner!!")
                print("*game over*")
                break
            elif myboard['7']==myboard['8']==myboard['9']!=' ':
                print_board(myboard)
                print(turn + " is the winner!!")
                print("*game over*")
                break
            elif myboard['1']==myboard['4']==myboard['7']!=' ':
                print_board(myboard)
                print(turn + " is the winner!!")
                print("*game over*")
                break
            elif myboard['2']==myboard['5']==myboard['8']!=' ':
                print_board(myboard)
                print(turn + " is the winner!!")
                print("*game over*")
                break
            elif myboard['3']==myboard['6']==myboard['9']!=' ':
                print_board(myboard)
                print(turn + " is the winner!!")
                print("*game over*")
                break
            elif myboard['1']==myboard['5']==myboard['9']!=' ':
                print_board(myboard)
                print(turn + " is the winner!!")
                print("*game over*")
                break
            elif myboard['3']==myboard['5']==myboard['7']!=' ':
                print_board(myboard)
                print(turn + " is the winner!!")
                print("*game over*")
                break
        if count==9:
            print("*game over*")
            print("tie match!!")
        if turn=='X':
            turn = 'O'
        else:
            turn = 'X'

    rematch = input("to play again select y or else n : ")
    if rematch=='y':
        for key in myboardkeys:
            myboard[key] = ' '

        
        mygame()

if __name__=="__main__":
    mygame()


