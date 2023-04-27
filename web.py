import streamlit as st
import functions

todos = functions.read_todos()

def add_todo():
    todo = st.session_state['new_todo'] +'\n'
    todos.append(todo)
    functions.write_todos(todos)




st.title("My ToDo App")
st.subheader("This is my todo app")
st.write("This app increase your activity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')

