def get_todos(filepath="file.txt"):
    with open("file.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath='file.txt'):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)