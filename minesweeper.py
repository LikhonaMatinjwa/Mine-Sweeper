# Create a function that will count the number of mines in the grid.
# Create a function that will assign the number of mines
# around a specific cell in the grid.
# Print the grid

def mines_around_cell(my_grid, row, col):
    count = 0
    rows, cols = len(my_grid), len(my_grid[0])

    # The for loops will iterate over cells adjacent to a given cell,
    # including both the cell itself and cells below and above it.
    # The range will ensure the starting index doesn't go below 0 and
    # above maximum number of rows/columns in the grid.
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if my_grid[i][j] == '#':
                count += 1

    return str(count)


def mines_around_grid(my_grid):

    rows, cols = len(my_grid), len(my_grid[0])
    mine_grid = [["#" for _ in range(cols)] for _ in range(rows)]

    # The mine_grid will assign the number of mines around a
    # specific cell in the grid.
    for row in range(rows):
        for col in range(cols):
            if my_grid[row][col] != '#':
                mine_grid[row][col] = mines_around_cell(my_grid, row, col)

    return mine_grid

my_grid = [["#", "-", "#", "-", "#"],
           ["-", "#", "-", "#", "-"],
           ["-", "-", "#", "-", "-"],
           ["-", "#", "#", "-", "-"],
           ["#", "#", "#", "-", "_"]]

mine_grid = mines_around_grid(my_grid)

# The map() function will convert each element in
# mine_grid into a string representation.
print("\n".join(map(str, mine_grid)))
