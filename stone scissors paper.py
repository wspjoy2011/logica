import tkinter as tk

WIN_WIDTH = 800
WIN_HEIGHT = 600


def print_value(value):
    print(value)


win = tk.Tk()
win.title('App')
win.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
win.bind('<Escape>', exit)

button = tk.Button(text='Click', font=('Arial', 13), command=lambda: print_value('Hello!'))
button.pack()

win.mainloop()
