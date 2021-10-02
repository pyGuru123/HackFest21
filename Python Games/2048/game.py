from Tkinter import Frame, Label, CENTER

import logic
import constant as c


class game2048(Frame):
    def __init__(self):
        Frame.__init__(self)  # creates frame for self (ie,game2048)

        self.master.iconbitmap("gameIcon.ico")
        self.grid()
        self.master.title("2048")
        self.master.bind("<Key>", self.key_down)
        self.commands = {
            c.KEY_UP: logic.upMove,
            c.KEY_DOWN: logic.downMove,
            c.KEY_LEFT: logic.leftMove,
            c.KEY_RIGHT: logic.rightMove
        }

        self.grid_cells= []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    

    def init_grid(self):
        background= Frame(self,bg=c.BG_COLOR_GAME,width=c.SIZE,height=c.SIZE)
        
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell= Frame(background,bg=c.BG_COLOR_CELL_EMPTY,width=c.SIZE/c.GRID_LEN,height=c.SIZE/c.GRID_LEN)

                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)

                t= Label(master=cell,text="",bg=c.BG_COLOR_CELL_EMPTY,justify=CENTER,font=c.FONT,width=5,height=2)

                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)
    

    def init_matrix(self):
        self.matrix=logic.startGame()
        logic.addNew2(self.matrix)
        logic.addNew2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number= self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(text="",bg=c.BG_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),bg=c.BG_COLOR_DICT[new_number],fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()




    
    def key_down(self,event):
        key= repr(event.char)
        # print(key)
        if key in self.commands:
            self.matrix,changed= self.commands[repr(event.char)](self.matrix)

            if changed:
                logic.addNew2(self.matrix)
                self.update_grid_cells()
                changed=False

                if logic.currStatus(self.matrix)=="Player won":
                    self.grid_cells[1][1].configure(text="YOU",bg=c.BG_COLOR_CELL_EMPTY)
                    self.grid_cells[2][2].configure(text="WON",bg=c.BG_COLOR_CELL_EMPTY)

                if logic.currStatus(self.matrix)=="Player lost":
                    self.grid_cells[1][1].configure(text="YOU",bg=c.BG_COLOR_CELL_EMPTY)
                    self.grid_cells[2][2].configure(text="LOST",bg=c.BG_COLOR_CELL_EMPTY)


gamegrid= game2048()
