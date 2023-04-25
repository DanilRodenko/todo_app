import functions
import time

now = time.strftime("%h %d %Y, %H:%m:%S")
print(now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith('add '):
        todo = user_action[4:].capitalize()

        todos = functions.read_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)


    elif user_action.startswith('show'):
        todos = functions.read_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}.{item}')


    elif user_action.startswith('edit '):
        try:
            number = int(user_action[5:]) - 1

            todos = functions.read_todos()

            new_todo = input("Enter new todo: ").capitalize()
            todos.__setitem__(number, new_todo + '\n')

            functions.write_todos(todos)
        except ValueError:
            print('Invalid command')
            continue
        except IndexError:
            print('There is no item with this number')
            continue

    elif user_action.startswith('complete '):
        try:
            number = int(user_action[9:]) - 1

            todos = functions.read_todos()

            complete_todo = todos[number].strip('\n')
            todos.pop(number)


            functions.write_todos(todos)

            print(f"""Todo {complete_todo} remove from the list""")
        except IndexError:
            print('There is no item with this number')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Command is not valid')


print('Bye')