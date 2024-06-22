while True:
    user_action = input("Type add, show, edit, complete or exit:")
    if 'add' in user_action:
        todo = user_action[4:]
        todo = input("Enter a todo: ") + "\n"
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        for index, items in enumerate(todos):
            items = items.strip('\n')
            row = f"{index + 1}-{items}"
            print(row)
    elif 'edit' in user_action:
        number = int(input("the no. of todo to edit"))
        number = number - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            print('here is todos existing', todos)
        new_todo = input("Enter a new todo")
        todos[number] = new_todo + '\n'
        print('Here is how it will be', todos)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number = int(input("the no. of todo to complete"))
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index]
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    message = f"Todo {todo_to_remove} was removed from the list"
    print(message)
