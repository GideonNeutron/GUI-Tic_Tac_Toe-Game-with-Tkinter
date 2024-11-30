from tkinter import *

playerX_wins = 0
playerO_wins = 0

def callback(r,c):
    global player
    if player == 'X' and states[r][c] == 0 and stop_game==False:
        b[r][c].configure(text='X', fg='red')
        states[r][c] = 'X'
        player = 'O'
    if player == 'O' and states[r][c] == 0 and stop_game==False:
        b[r][c].configure(text='O', fg='blue')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()

    player_turn.configure(text="Player {}'s turn.".format(player))

def check_for_winner():
    global stop_game
    global playerX_wins
    global playerO_wins
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            if states[i][0] == 'X' and stop_game==False:
                playerX_wins += 1
            elif states[i][0] == 'O' and stop_game==False:
                playerO_wins += 1
            b[i][0].configure(bg='gold')
            b[i][1].configure(bg='gold')
            b[i][2].configure(bg='gold')
            stop_game = True
            
    for i in range(3):
        if states[0][i]==states[1][i]==states[2][i]!=0:
            if states[0][i] == 'X' and stop_game==False:
                playerX_wins += 1
            elif states[0][i] == 'O' and stop_game==False:
                playerO_wins += 1
            b[0][i].configure(bg='gold')
            b[1][i].configure(bg='gold')
            b[2][i].configure(bg='gold')
            stop_game = True

    if states[0][0]==states[1][1]==states[2][2]!=0:
        if states[0][0] == 'X' and stop_game==False:
            playerX_wins += 1
        elif states[0][0] == 'O' and stop_game==False:
            playerO_wins += 1
        b[0][0].configure(bg='gold')
        b[1][1].configure(bg='gold')
        b[2][2].configure(bg='gold')
        stop_game = True
        
    if states[2][0]==states[1][1]==states[0][2]!=0:
        if states[2][0] == 'X' and stop_game==False:
            playerX_wins += 1
        elif states[2][0] == 'O' and stop_game==False:
            playerO_wins += 1
        b[2][0].configure(bg='gold')
        b[1][1].configure(bg='gold')
        b[0][2].configure(bg='gold')
        stop_game = True
    
    game_stat.configure(text='Player_X   {} -- {}   Player_O'.format(playerX_wins, playerO_wins))


def restart():
    global stop_game
    for r in range(3):
        for c in range(3):
            b[r][c].configure(text='', bg='white')
            states[r][c] = 0
    stop_game = False

root = Tk()

b = [['','',''],
    ['','',''],
    ['','','']]

states = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=3, bg='white', command = lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row = i, column = j)

player = 'X'
stop_game = False

welcome = Label(text='WELCOME !!!', bg='white', font=('Franklin', 30, 'bold underline'), width=18, fg='red')
welcome.grid(row = 3, column=0, columnspan=3)

player_turn = Label(text="Player {}'s turn.".format(player), bg='white',fg='blue', font=('Franklin', 10, 'bold'), width=55)
player_turn.grid(row = 5, column=0, columnspan=3)

game_stat = Label(text='Player_X   {} -- {}   Player_O'.format(playerX_wins, playerO_wins), bg='white', font=('Franklin', 20, 'bold'), width=26)
game_stat.grid(row = 4, column=0, columnspan=3)

restart_button = Button(text = 'Restart Game', bg = 'red', fg='white', width=40, font = ('Arial', 14), command=restart)
restart_button.grid(row = 6, column=0, columnspan=3)  


mainloop()