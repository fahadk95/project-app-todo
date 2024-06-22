def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos.local = file_local.readlines()
    return todos.local


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()

    if user_action.startswith("add"):
        new_todo = user_action[4:].strip()
        if new_todo:
            todos = get_todos('todos.txt')
            todos.append(new_todo + '\n')
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

    elif user_action.startswith("show"):
        if len(user_action) == 4:  # "show"
            todos = get_todos('todos.txt')
            for index, todo in enumerate(todos):
                todo = todo.strip('\n')
                print(f"{index + 1}-{todo}")
        else:  # "show <number>"
            try:
                number = int(user_action[5:])
                todos = get_todos('todos.txt')
                if 1 <= number <= len(todos):
                    new_todo = input("Enter a new todo: ") + '\n'
                    todos[number - 1] = new_todo

                    with open('todos.txt', 'w') as file:
                        file.writelines(todos)
                else:
                    print("Invalid todo number. Please enter a valid number.")
            except ValueError:
                print("Your command is not valid")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos('todos.txt')

            if 1 <= number <= len(todos):
                todo_to_remove = todos[number - 1]
                todos.pop(number - 1)
                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
                message = f"Todo '{todo_to_remove.strip()}' was removed from the list."
                print(message)
            else:
                print("Invalid todo number. Please enter a valid number.")
        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("There is no item with that number")

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input. Please type add, show, edit, complete or exit.")
