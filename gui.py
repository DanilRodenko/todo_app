import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme("Black")
clock = sg.Text("", key='clock')
label = sg.Text("Type in to-do")

input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
list_box = sg.Listbox(values=functions.read_todos(), size=(45, 10),
                   key='todos', enable_events=True)

add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box],
                           [list_box],
                           [add_button, edit_button, complete_button, exit_button]],
                   font=('Times New Roman', 17))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%h %d %Y, %H:%m:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(values = todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.read_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)

                window['todos'].update(values = todos)
            except IndexError:
                sg.popup("Please selecet an itme first")
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]

                todos = functions.read_todos()

                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select an item first')

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

        case 'Exit':
            break


window.close()
