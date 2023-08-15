import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")

# key will change the key from number to the text we identify
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

# if you add items in 1 list : they will be in 1 row layout=[[label, input_box]]
#  layout=[[label], [input_box]] will show in 2 rows
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print("Hello")
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
    if event == sg.WIN_CLOSED:
        break

window.close()