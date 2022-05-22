# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её
 
from tkinter import *
 
player = 1
 
 
def line_done():
    if game_dict['00'] != 0 and game_dict['00'] == game_dict['01'] == game_dict['02']:
        game_canvas.create_line(25, 50, 275, 50, width=5, fill='blue')
        return True
    elif game_dict['10'] != 0 and game_dict['10'] == game_dict['11'] == game_dict['12']:
        game_canvas.create_line(25, 150, 275, 150, width=5, fill='blue')
        return True
    elif game_dict['20'] != 0 and game_dict['20'] == game_dict['21'] == game_dict['22']:
        game_canvas.create_line(25, 250, 275, 250, width=5, fill='blue')
        return True
    elif game_dict['00'] != 0 and game_dict['00'] == game_dict['10'] == game_dict['20']:
        game_canvas.create_line(50, 25, 50, 275, width=5, fill='blue')
        return True
    elif game_dict['01'] != 0 and game_dict['01'] == game_dict['11'] == game_dict['21']:
        game_canvas.create_line(150, 25, 150, 275, width=5, fill='blue')
        return True
    elif game_dict['02'] != 0 and game_dict['02'] == game_dict['12'] == game_dict['22']:
        game_canvas.create_line(250, 25, 250, 275, width=5, fill='blue')
        return True
    elif game_dict['00'] != 0 and game_dict['00'] == game_dict['11'] == game_dict['22']:
        game_canvas.create_line(25, 25, 275, 275, width=5, fill='blue')
        return True
    elif game_dict['02'] != 0 and game_dict['02'] == game_dict['11'] == game_dict['20']:
        game_canvas.create_line(275, 25, 25, 275, width=5, fill='blue')
        return True
 
def clicked(event):
    global player
    x = event.x // 100 * 100
    y = event.y // 100 * 100
    position = str(event.y // 100) + str(event.x // 100)
    if game_dict[position] == 0 and not line_done():
        if player == 1:
            game_canvas.create_line(x + 20, y + 20, x + 80, y + 80, width=5, fill='red')
            game_canvas.create_line(x + 20, y + 80, x + 80, y + 20, width=5, fill='red')
            game_dict[position] = player
            player = 2
        else:
            game_canvas.create_oval(x + 20, y + 20, x + 80, y + 80, width=5, outline='green')
            game_dict[position] = player
            player = 1
    if line_done():
        panel.configure(text="Winner")
 
# Словарь с игровым полем. Изначально нули в каждой клетке
game_dict = {'00': 0, '01': 0, '02': 0,
             '10': 0, '11': 0, '12': 0,
             '20': 0, '21': 0, '22': 0}
field = Tk()
field.title('Крестики - нолики')
field.geometry('310x400')
game_canvas = Canvas(field, height=300, width=300, background='white')
game_canvas.create_line(100, 5, 100, 295, fill='lightgrey')
game_canvas.create_line(200, 5, 200, 295, fill='lightgrey')
game_canvas.create_line(5, 100, 295, 100, fill='lightgrey')
game_canvas.create_line(5, 200, 295, 200, fill='lightgrey')
 
game_canvas.bind('<Button>', clicked)
game_canvas.pack()
panel = Label(field, font=("Verdana", 20), text="Let's game!")
panel.pack()
 
field.mainloop()