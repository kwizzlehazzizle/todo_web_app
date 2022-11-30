import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+'\n')
    functions.write_todos(todos)

#Run the following in terminal
#streamlit run web.py


st.title("My Todo App")
st.subheader("This is my todo app")
for i,todo in enumerate(todos):
    todo_key = str(i)+'_'+todo
    checkbox = st.checkbox(todo,key= todo_key)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        print(st.session_state)
        del st.session_state[todo_key]
        print(st.session_state)
        st.experimental_rerun()
        print(st.session_state)
st.text_input(label="Enter a todo:", placeholder="Add a new todo: ",
              on_change=add_todo, key='new_todo')


#st.session_state