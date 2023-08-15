from functions import get_todos, write_todos
import time

while True:
    # Add Datetime
    print(f'It is {time.strftime("%b %d, %Y %H:%M:%S")}')

    # Get user input and strip space chars
    user_action = input("Type add, show, edit, complete,  or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        # read existing todo list from a file
        todos = get_todos()

        todos.append(todo + '\n')

        # store item in text file
        write_todos(todos, 'todos.txt')

    elif user_action.startswith('show'):
        todos = get_todos('todos.txt')

        # remove \n from the list
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            # create a list from file
            todos = get_todos()

            new_todo = input("what is your new todo: ")
            todos[number - 1] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print('There is no item with that index')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid.')
print("Bye!")