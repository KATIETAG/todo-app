import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")

# key will change the key from number to the text we identify
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# if you add items in 1 list : they will be in 1 row layout=[[label, input_box]]
#  layout=[[label], [input_box]] will show in 2 rows
window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        #refresh todo list instantly
        window['todos'].update(values=todos)
    if event == "Edit":
        todo_to_edit = values['todos'][0]
        new_todo = values['todo'] +"\n"

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        # refresh window in real time
        window['todos'].update(values=todos)
        #put current selection in text box
    if event == 'Complete':
        todo_to_complete = values['todos'][0]
        todos = functions.get_todos()
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        # remove item from the list box
        window['todos'].update(values=todos)
        # clean the text box
        window['todo'].update(value='')
    if event == "Exit":
        break


    if event == 'todos':
        window['todo'].update(value=values['todos'][0])

    if event == sg.WIN_CLOSED:
        break

window.close()