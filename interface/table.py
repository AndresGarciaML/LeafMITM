import tkinter as tk
from map_gestion.cell import Cell
import logging

# source https://github.com/XeLiT

class Table(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)
        self._widgets = []
        self.cells = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text=" ", borderwidth=0, width=5)
                if row % 2  == 0:
                    label.grid(row=row, column=column, sticky="nsew", padx=0, pady=0)
                else:
                    label.grid(row=row, column=column, sticky="nsew", padx=0, pady=0)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=3)

    def set_background(self, row, column, color):
        widget = self._widgets[row][column]
        widget.configure(background=color)

    def set_data(self, cells: [[Cell]]):
        self.cells = cells
        cellID = 0
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                cellID += 1
                cell = cells[i][j]
                widget = self._widgets[i][j]
                
                widget.configure(background=cell.color, text=str(cell.CellID))
                widget.bind('<Button-1>', lambda e, a=i, b=j: self.debug_cell(a, b))

    def debug_cell(self, i, j):
        print(self.cells[i][j].__dict__)
