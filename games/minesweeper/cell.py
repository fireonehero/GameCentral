import random
from tkinter import *

import games.minesweeper.colors as colors
import games.minesweeper.settings as settings

#Returns the cell's (x,y) coordinates
def get_cell_by_axis(x, y):
    for cell in Cell.all:
        if cell.x_pos == x and cell.y_pos == y:
            return cell

#Popup to display upon winning
def win_popup():
    popup = Toplevel()
    popup.title("Congratulations")
    popup.geometry("100x100")
    label = Label(popup, text="You Win!")
    label.pack()
    close_button = Button(popup, text="Close", command=popup.destroy)
    close_button.pack()

#Popup to display upon losing
def lose_popup():
    popup = Toplevel()
    popup.title("Failure")
    popup.geometry("100x100")
    label = Label(popup, text="You Lose")
    label.pack()
    close_button = Button(popup, text="Close", command=popup.destroy)
    close_button.pack()

#Popup to display upon almost succeeding
def almost_popup():
    popup = Toplevel()
    popup.title("Almost There")
    popup.geometry("100x100")
    label = Label(popup, text="Try Again!")
    label.pack()
    close_button = Button(popup, text="Close", command=popup.destroy)
    close_button.pack()

#Creates holding variable for all the individual mines to be stored
def init_mines():
    global flagged_mines
    global flagged_mines_bomb_status
    global is_player_alive
    is_player_alive = True
    flagged_mines = 0
    flagged_mines_bomb_status = []
    Cell.all = []

#Varibales for stuff and things
flagged_mines = 0
flagged_mines_bomb_status = []

is_player_alive = True

cell_clicked_mine_count = 0

#Class with information about the cells
class Cell:
    all = []

    #Create a single mine with it's own unique variables,
    #and upload the variables to the list of cells
    def __init__(self, x_pos, y_pos, bomb_id=0, is_bomb=False, is_flagged=False, is_clicked=False):
        self.is_clicked = is_clicked
        self.cell_btn_object = None
        self.is_flagged = is_flagged
        self.is_bomb = is_bomb
        self.bomb_id = bomb_id
        self.y_pos = y_pos
        self.x_pos = x_pos

        Cell.all.append(self)

    #Create a button for a single mine
    def create_btn_object(self, location):
        custom_font = ("Microsoft Sans Serif", 8, "bold")
        btn = Button(
            location,
            font=custom_font,
            bg=colors.WHITE,
            width=settings.CELL_SIZE * 2,
            height=settings.CELL_SIZE,
            relief="raised",
            borderwidth=5
        )
        btn.bind('<Button-1>', self.select_mine)
        btn.bind('<Button-3>', self.flag_mine)
        self.cell_btn_object = btn

    #When the mine is clicked on
    def select_mine(self, event):
        self.is_clicked = True
        #Check player is still playing
        if is_player_alive:
            print(event)
            #Check if cell is flagged
            if self.is_flagged:
                pass
            #If cell isn't flagged proceed with the game
            elif not self.is_flagged:
                #If the cell is a mine: end game
                if self.is_bomb:
                    self.show_mine()
                    lose_popup()
                #If the cell is not a mine: show how many mines are adjacent
                elif not self.is_bomb:
                    print(self.is_clicked)
                    self.show_cell()
        #If player isn't alive do nothing
        elif not is_player_alive:
            pass

    #Reveal all mines on the board
    def show_mine(self):
        global is_player_alive
        is_player_alive = False
        self.is_flagged = False
        self.cell_btn_object.configure(bg=colors.RED, text='')
        for cell in self.all:
            if cell.is_bomb:
                cell.cell_btn_object.configure(bg=colors.RED, text='')
                if cell.is_flagged:
                    cell.cell_btn_object.configure(
                        text='F',
                        fg=colors.BLACK_7
                    )

    #Calculate how many mines are surrounding the selected cell
    @property
    def get_surrounded_cells(self):
        #List of all positions relative to the selected cell to check
        surrounded_cells = [
            get_cell_by_axis(self.x_pos - 1, self.y_pos - 1),
            get_cell_by_axis(self.x_pos - 1, self.y_pos),
            get_cell_by_axis(self.x_pos - 1, self.y_pos + 1),
            get_cell_by_axis(self.x_pos, self.y_pos - 1),
            get_cell_by_axis(self.x_pos, self.y_pos + 1),
            get_cell_by_axis(self.x_pos + 1, self.y_pos - 1),
            get_cell_by_axis(self.x_pos + 1, self.y_pos),
            get_cell_by_axis(self.x_pos + 1, self.y_pos + 1)
        ]
        #Find and return each surrounding cell
        surrounded_cells = [cell for cell in surrounded_cells if cell is not None]
        return surrounded_cells

    #Return the amount of mines surrounding the selected cell
    def surrounding_mines(self):
        global cell_clicked_mine_count
        mines = 0
        #Check each surrounded cell and if it's a mine add one to the mine count
        for cell in self.get_surrounded_cells:
            if cell.is_bomb:
                mines += 1
        cell_clicked_mine_count = mines
        return mines

    #Check to make sure that the clicked cell is surrounding mines, isn't clicked, nor flagged
    @property
    def surrounded_cells_mines_length(self):
        mines = 0
        for cell in self.get_surrounded_cells:
            #If adjacent cell is a mine add to mine count
            if cell.is_bomb:
                mines += 1
                print(f'Surrounding Mines: {cell.surrounding_mines()}')
            #If adjacent cell isn't clicked, nor flagged, and isn't touching any mines
            elif not cell.is_clicked and not cell.is_flagged and self.surrounding_mines() == 0:
                print(cell)
                cell.is_clicked = True
                cell.show_cell()

        return mines

    #When cell is being revealed, such as clicked by player or next to empty cell
    def show_cell(self):
        #Dictionary of each number to a color, like in actual minesweeper
        switch_dict = {
            1: colors.BLUE_1,
            2: colors.GREEN_2,
            3: colors.RED_3,
            4: colors.DARK_BLUE_4,
            5: colors.MAROON_5,
            6: colors.CYAN_6,
            7: colors.BLACK_7,
            8: colors.GREY_8
        }

        #If there are mines around cell
        if self.surrounded_cells_mines_length != 0:
            self.cell_btn_object.configure(
                text=self.surrounded_cells_mines_length,
                bg=colors.GREY,
                fg=switch_dict.get(self.surrounded_cells_mines_length, colors.BLACK_7)
            )

        #If there are no mines around cell
        elif self.surrounded_cells_mines_length == 0:
            self.cell_btn_object.configure(
                bg=colors.DARK_GREY,
                fg=switch_dict.get(self.surrounded_cells_mines_length, colors.BLACK_7)
            )

    #When the player flags the cell via right click
    def flag_mine(self, event):
        #Fist make sure player is still alive
        if is_player_alive:
            print(event)
            global flagged_mines
            global flagged_mines_bomb_status

            #If the cell is not flagged, the amount of flagged cells don't equal the bomb count, and the cell has not been revealed
            if not self.is_flagged and flagged_mines != settings.MINE_COUNT and not self.is_clicked:
                #Add the the flagged mines amount
                flagged_mines += 1
                #Change the button's appearance
                self.cell_btn_object.configure(
                    text='F',
                    bg=colors.GREEN,
                    fg=colors.BLACK_7
                )
                #Update cell state
                self.is_flagged = True
                #Add if cell is a bomb to an array the check if the player has won (Used later)
                flagged_mines_bomb_status.append(self.is_bomb)

                #If the max amount of flags have been placed down
                if flagged_mines == settings.MINE_COUNT:
                    #If all the flagged cells are mines player wins
                    if flagged_mines_bomb_status.count(True) == settings.MINE_COUNT:
                        win_popup()
                    #If all the flagegd cells are not mines, player keeps playing
                    elif flagged_mines_bomb_status.count(True) != settings.MINE_COUNT:
                        almost_popup()
                    pass
            #If the cell is not flagged, but the player cannot put down any more flags
            elif not self.is_flagged and flagged_mines > settings.MINE_COUNT:
                pass
            #If the cell is flagged then un-flag it
            elif self.is_flagged:
                flagged_mines -= 1
                self.cell_btn_object.configure(
                    text='',
                    bg=colors.WHITE
                )
                self.is_flagged = False
                #Adjust the array to make it make sense based on the user's previous action
                if not self.is_bomb:
                    flagged_mines_bomb_status.remove(False)
                elif self.is_bomb:
                    flagged_mines_bomb_status.remove(True)
            #If player isn't alive, don't do anythin
            elif not is_player_alive:
                pass

    #Randomly select cells to be a mine
    @staticmethod
    def randomize_mines():
        cycling = True
        picked_cells = []
        print(f'Cells: {Cell.all}\nBomb Count: {settings.MINE_COUNT}')
        #Grab a random sample of cells to change to mines
        while cycling:
            picked_cells = random.sample(
                Cell.all,
                settings.MINE_COUNT
            )
            print(f'Selected Cells:{picked_cells}\nCount: {len(picked_cells)}')
            #I'm not even going to try to decipher this, your guess is as good as mine 
            if not str(picked_cells).__contains__(f"Cell(0, 0)") and not str(picked_cells).__contains__(f"Cell({settings.GRID_SIZE - 1}, 0)") and not str(picked_cells).__contains__(f"Cell(0, {settings.GRID_SIZE - 1})") and not str(picked_cells).__contains__(f"Cell({settings.GRID_SIZE - 1}, {settings.GRID_SIZE - 1})"):
                cycling = False
        #Change all the selected cells to mines
        for picked_cells in picked_cells:
            picked_cells.is_bomb = True

    #return the coordinates of the cell
    def __repr__(self):
        return f'Cell({self.x_pos}, {self.y_pos})'
