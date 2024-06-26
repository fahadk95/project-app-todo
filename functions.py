def get_todos(filepath="todos.txt"):
    """" Read the text file and returns the list of
        to-do items
        """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """" Write the to-do item list in the text file   """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
