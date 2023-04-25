import functions
import PySimpleGUI as sg

label = sg.Text("Type in to-do")

input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
list_box = sg.Listbox(values=functions.read_todos(), size=(45, 10),
                   key='todos', enable_events=True)

add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box],
                           [list_box],
                           [add_button, edit_button, complete_button]],
                   font=('Times New Roman', 17))

while True:
    event, values = window.read()
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
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.read_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)

            window['todos'].update(values = todos)

        case 'Complete':
            todo_to_complete = values['todos'][0]

            todos = functions.read_todos()
            index = todos.index(todo_to_complete)
            todos.pop(index)
            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
