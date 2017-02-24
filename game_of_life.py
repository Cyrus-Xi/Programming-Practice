#!/usr/bin/env python

import random

class Cell:
    
    def __init__(self, state='Rand'):
        # alive:dead = True:False
        if state == 'Rand': self.state = random.choice([True, False])
        else: self.state = state
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state
    
    def __str__(self):
        if self.state: return '[X]'
        else: return '[ ]'

def print_grid(grid):
     for row in grid:
        row_str = ''
        for cell in row:
            if cell.get_state(): row_str += '[X]'
            else: row_str += '[ ]'
        print row_str

"""        
[ ][X][ ][ ][X]
[ ][ ][ ][X][X]
[ ][ ][ ][ ][ ]
[ ][X][ ][ ][X]
[ ][ ][X][X][X]
TICK 4

[ ][ ][ ][ ][ ]
[X][ ][ ][X][X]
[X][ ][ ][X][X]
[X][ ][X][ ][X]
[X][ ][X][X][X] 
"""

def initialize_grid(size=5, state=None):
    grid = []
    for i in xrange(size):
        row = []
        for j in xrange(size):
            if state == 'False': curr = Cell(state=False)
            elif state == 'True': curr = Cell(state=True)
            else: curr = Cell()
            row.append(curr)
        grid.append(row)
        
    return grid
    
def apply_rule(count_alive, cell):
    if cell.get_state():
        if count_alive < 2 or count_alive > 3:
            return False
    elif count_alive == 3:
            return True
    
def get_neighbor_live_count(grid, row_i, col_i):
    neighbor_indices = [(row_i-1, col_i-1), (row_i-1, col_i), 
                            (row_i-1, col_i+1), (row_i, col_i-1),
                            (row_i, col_i+1), (row_i+1, col_i-1),
                            (row_i+1, col_i), (row_i+1, col_i+1)]
    # Don't wrap around.
    neighbor_indices = [(x, y) for x, y in neighbor_indices if x > -1 
                                    and y > -1]
    
    count_alive = 0
    for cell_row, cell_col in neighbor_indices:
        try:
            neighbor = grid[cell_row][cell_col]
            if neighbor.get_state(): count_alive += 1
        # Went off the grid.
        except IndexError as e:
            continue
            
    return count_alive
    
def game_of_life_sim(ticks=20, grid=None):
    if not grid: grid = initialize_grid()
    
    print_grid(grid)
        
    for i, tick in enumerate(xrange(ticks)):
        changes = []
        print '\nTICK {}'.format(str(i))
        
        for row_i, row in enumerate(grid):
            for col_i, curr in enumerate(row):
                count_alive = get_neighbor_live_count(grid, row_i, col_i)
                
                new_state = apply_rule(count_alive, curr)
                # Keep track of changes and apply them all at once at the end.
                if new_state is not None and new_state != curr.get_state():
                    changes.append((row_i, col_i, new_state))
                        
        # Update cells.
        for ch_r, ch_c, st in changes:
            grid[ch_r][ch_c].set_state(st)
                 
        print_grid(grid)
        
game_of_life_sim(5)

# Test using blinker pattern.
blinker_grid = initialize_grid(state='False')

for i in xrange(1, 4):
    blinker_grid[2][i].set_state(True)

assert get_neighbor_live_count(blinker_grid, 2, 1) == 1
assert get_neighbor_live_count(blinker_grid, 2, 2) == 2
assert get_neighbor_live_count(blinker_grid, 2, 3) == 1
assert get_neighbor_live_count(blinker_grid, 0, 4) == 0

assert apply_rule(2, blinker_grid[2][2]) is None
assert not apply_rule(1, blinker_grid[2][1]) 
assert not apply_rule(1, blinker_grid[2][3]) 
assert apply_rule(3, blinker_grid[1][2])

print
game_of_life_sim(ticks=5, grid=blinker_grid)
