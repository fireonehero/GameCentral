from tkinter import *

from games.minesweeper.cell import Cell, init_mines
import games.minesweeper.colors as colors
import games.minesweeper.settings as settings
import games.minesweeper.utils as utils

#Create the variables that'll be used to set up the game
difficulty_scale = None
top_frame = None
center_frame = None
game_frame = None
root = None

#Restart the game
def restart_game():
    #If the grid size has been altered recreate the window
    if difficulty_scale.get() != settings.GRID_SIZE:
        settings.set_grid_size(difficulty_scale.get())
        refresh_window(root)
        init_mines()
        init_game()
    #If the same difficulty is being used
    elif difficulty_scale.get() == settings.GRID_SIZE:
        init_game()

#Create the game window
def init_window():
    global root
    global top_frame
    global center_frame
    global game_frame
    global difficulty_scale
    root = Tk()
    root.configure(bg=colors.GREY)
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.title("Minesweeper")
    root.resizable(False, False)

    #Game Manager
    top_frame = Frame(
        root,
        width=settings.WIDTH,
        height=utils.get_percent(settings.HEIGHT, 15),
        borderwidth=5,
        relief='groove'
    )
    #Minesweeper field holder
    center_frame = Frame(
        root,
        width=settings.WIDTH,
        height=utils.get_percent(settings.HEIGHT, 85),
        borderwidth=5,
        background=colors.GREY,
        relief='raised'
    )
    #Minesweeper field
    game_frame = Frame(
        root,
        borderwidth=5,
        relief='raised'
    )
    #Place down buttons, grids, sliders, etc.
    custom_font = ("Microsoft Sans Serif", 8, "bold")
    restart_btn = Button(
        top_frame,
        text="Restart?",
        font=custom_font,
        bg=colors.WHITE,
        width=7,
        height=2,
        relief="raised",
        borderwidth=5,
        command=restart_game
    )
    difficulty_scale = Scale(
        root,
        from_=5,
        to=16,
        orient=HORIZONTAL
    )

    #Set the grid size to match the slider
    difficulty_scale.set(settings.GRID_SIZE)

    top_frame.place(x=0, y=0)
    center_frame.place(x=0, y=utils.get_percent(settings.HEIGHT, 20))
    game_frame.winfo_width()
    game_frame.place(in_=center_frame, anchor='center', relx=.5, rely=.5)

    restart_btn.place(in_=top_frame, anchor='w', relx=.51, rely=.5)
    difficulty_scale.place(in_=top_frame, anchor='e', relx=.49, rely=.5)

#Start the game up
def init_game():
    init_mines()
    #Place a mine in every (x,y)
    for y in range(settings.GRID_SIZE):
        for x in range(settings.GRID_SIZE):
            c1 = Cell(x, y)
            c1.create_btn_object(game_frame)
            c1.cell_btn_object.grid(
                column=x,
                row=y
            )

    Cell.randomize_mines()

#Recreate window, used if difficulty is altered and screen resize is needed
def refresh_window(self):
    self.destroy()
    init_window()


# Run the window
def play_game():
    init_window()
    init_game()
    root.mainloop()