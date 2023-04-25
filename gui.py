import functions
import PySimpleGUI as sg

label = sg.Text("Type in to-do")

input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button('Add todo')

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
