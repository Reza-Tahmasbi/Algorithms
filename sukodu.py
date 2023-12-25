def read_grid():
    with open(r"filename.txt", 'r') as file:
        lines = file.readlines()
        grid = [[int(ch) for ch in line.replace('\n','')] for line in lines]
    return grid
    
    
def is_valid(grid, r, c, k):
    in_row = k in grid[r] # check if selected number is already in the row
    in_column = k in [grid[i][c] for i in range(9)] # check if the selected number is already in the column
    in_box = k in [grid[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)] # check if the selected number is 9-cells
    return not in_row and not in_column and not in_box


def solve(grid, r=0, c=0):
    if r == 9:
        return True
    elif c == 9:
        return solve(grid,r+1, 0)
    elif grid[r][c] !=0:
        return solve(grid, r, c+1)
    else:
        for k in range(1, 10):
            if is_valid(grid, r, c,k):
                grid[r][c] = k
                if solve(grid, r, c+1):
                        return True
                grid[r][c] = 0
        return False

def print_grid(grid):
    for row in grid:
        print(row)
        

if __name__ == '__main__':
    grid = read_grid()
    print("The Previous Grid:")
    print_grid(grid)
    if solve(grid) == True:
        print("\nBackTracking... BOOM!")
        print("\nSolved Grid: ")
        print_grid(grid)
    with open(r"C:\Users\reza\Desktop\test.txt", 'w') as f:
        f.write('\n'.join([' '.join([str(cell) for cell in row]) for row in grid]))
    
        

