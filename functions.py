FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    # read existing todo list from a file
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        """ write to-do item list in the text file."""
        todos_local = file_local.readlines()  # store the file in a list
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# only see the function when we execute this code directly and not when we run main
if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())