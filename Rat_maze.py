import random
from termcolor import colored
def generate_maze(n):
    arr = [[colored("◌", "blue") for _ in range(n)] for _ in range(n)]
    size = n * n // 4
    for i in range(size):
        arr[0][0] = 'S'
        arr[n - 1][n - 1] = 'E'
        x, y = random.randint(0, n - 1), random.randint(0, n - 1)
        if (x == 0 and y == 0) or (x == n - 1 and y == n - 1) or (x == 0 and y == 1) or (x == n - 2 and y == n - 1):
            continue
        arr[x][y] = colored('▓', 'red')
    return arr
def print_maze(maze):
    for i in range(len(maze)):
        box = ''
        for k in range(len(maze)):
            box += "+---"
        print(colored(box + "+", "red"))

        print('| ', end='')
        for j in range(len(maze)):
            print(maze[i][j], end=" | ")
        print()
    box = ''
    for t in range(len(maze)):
        box += "+---"
    print(colored(box + "+", "red"))
def path():
    pass
def main():
    n = int(input('Enter the size of the maze (nxn): '))
    maze = generate_maze(n)
    
    print_maze(maze)
    
    print('1. Print the path')
    print('2. Generate another puzzle')
    print('3. Exit the Game')
    choice = int(input('Enter your choice (1/2/3): '))
    
    if choice == 1:
        path_found = path(maze, 0, 1)
        print_maze(path_found)
    elif choice == 2:
        main()
    elif choice == 3:
        return
    else:
        print('Invalid Choice')

main()
