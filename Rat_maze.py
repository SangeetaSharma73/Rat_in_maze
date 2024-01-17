def generate_maze(n):
    pass
def print_maze(maze):
    pass
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
