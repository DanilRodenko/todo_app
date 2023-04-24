FILEPATH = 'todos.txt'

def read_todos(filepath = FILEPATH):
    """Read the txt file and return
    list of to-do items"""

    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos


def write_todos(todos_args, filepath = FILEPATH):
    """Write the to-do items in txt files"""

    with open(filepath, 'w') as file:
        file.writelines(todos_args)

if __name__ == '__main__':
    print('Hello')
    print(read_todos())