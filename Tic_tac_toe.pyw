__author__ = "Dhanalakshmi Narala"

"""A simple tic tac toe desktop application using python package tkinter."""

from tkinter import *

user = "X"
filled = 0


def create_buttons(window):
    button_11 = Button(window, text="", width=5, height=2, command=lambda: click(button_11, buttons))
    button_11.grid(column=0, row=1)
    button_12 = Button(window, text="", width=5, height=2, command=lambda: click(button_12, buttons))
    button_12.grid(column=1, row=1)
    button_13 = Button(window, text="", width=5, height=2, command=lambda: click(button_13, buttons))
    button_13.grid(column=2, row=1)

    button_21 = Button(window, text="", width=5, height=2, command=lambda: click(button_21, buttons))
    button_21.grid(column=0, row=2)
    button_22 = Button(window, text="", width=5, height=2, command=lambda: click(button_22, buttons))
    button_22.grid(column=1, row=2)
    button_23 = Button(window, text="", width=5, height=2, command=lambda: click(button_23, buttons))
    button_23.grid(column=2, row=2)

    button_31 = Button(window, text="", width=5, height=2, command=lambda: click(button_31, buttons))
    button_31.grid(column=0, row=3)
    button_32 = Button(window, text="", width=5, height=2, command=lambda: click(button_32, buttons))
    button_32.grid(column=1, row=3)
    button_33 = Button(window, text="", width=5, height=2, command=lambda: click(button_33, buttons))
    button_33.grid(column=2, row=3)

    buttons = [[button_11, button_12, button_13],
               [button_21, button_22, button_23],
               [button_31, button_32, button_33]]
    return window


def click(button, buttons):
    global user
    if button['text'] == "":
        button.config(text=user)
    if user == "X":
        user = "O"
    else:
        user = "X"

    global filled
    filled += 1
    if filled == 9:
        values = convert_buttons_to_values(buttons)
        result = decide_winner(values)
        print(result)

def convert_buttons_to_values(buttons):
    values = []
    for row in buttons:
        temp_row = []
        for button in row:
            if button['text'] == "X":
                temp_row.append(1)
            else:
                temp_row.append(0)
        values.append(temp_row)
    return values

def decide_winner(values):
    result = ""
    if values[0][0] == values[0][1] and values[0][0] == values[0][2]:
        result = values[0][0]
    elif values[1][0] == values[1][1] and values[1][0] == values[1][2]:
        result = values[1][0]
    elif values[2][0] == values[2][1] and values[2][0] == values[2][2]:
        result = values[2][0]

    elif values[0][0] == values[1][0] and values[0][0] == values[2][0]:
        result = values[0][0]
    elif values[0][1] == values[1][1] and values[0][1] == values[2][1]:
        result = values[0][1]
    elif values[0][2] == values[1][2] and values[0][2] == values[2][2]:
        result = values[0][2]

    elif values[0][0] == values[1][1] and values[0][0] == values[2][2]:
        result = values[0][0]
    elif values[0][2] == values[1][1] and values[0][2] == values[2][0]:
        result = values[0][2]
    else:
         return "draw"
    if result == 1:
        return "USER 1"
    else:
        return "USER 2"


def app():
    root = Tk()
    root.title("Tic Tac Toe")
    root.geometry("200x200")
    root.resizable(height=False, width=False)
    root.config(padx=30, pady=20, bg="white")
    root = create_buttons(root)
    root.mainloop()

if __name__ == "__main__":
    app()
