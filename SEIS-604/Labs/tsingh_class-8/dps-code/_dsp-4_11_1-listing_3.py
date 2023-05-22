# _dsp-4_11_1-listing3.py

def search_from(maze, row, column):

    # Try each of four directions from this point until we find a way out.

    maze.update_position(row, column)

    # Base Case return values:

    #  1. We have run into an obstacle, return false

    if maze[row][column] == OBSTACLE:

        return False

    #  2. We have found an already explored square

    if maze[row][column] in [TRIED, DEAD_END]:

        return False

    # 3. We have found an exit

    if maze.is_exit(row, column):

        maze.update_position(row, column, PART_OF_PATH)

        return True

    maze.update_position(row, column, TRIED)

    # Otherwise, use logical short circuiting to try each direction

    # in turn (if needed)

    found = (

        search_from(maze, row - 1, column)

        or search_from(maze, row + 1, column)

        or search_from(maze, row, column - 1)

        or search_from(maze, row, column + 1)

    )

    if found:

        maze.update_position(row, column, PART_OF_PATH)

    else:

        maze.update_position(row, column, DEAD_END)

    return found