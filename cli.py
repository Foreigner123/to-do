from functions import get_todos, write_todo

while True:
    todos = get_todos()

    user_input = input("Type add, show, edit, exit or clear: ")
    user_input = user_input.strip().lower()

    if user_input.startswith("add"):
        new_todo = user_input[4:] or input("Enter a new todo: ")
        todos.append(new_todo + "\n")
        write_todo(todos)
    elif "show" in user_input:
        if todos:
            for i, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{i + 1} - {item.title()}")
        else:
            print("The todo list is empty")
    elif user_input.startswith("edit"):
        if todos:
            item_to_edit = user_input[5:] or input("Enter the item you want to add: ") + "\n"
            if item_to_edit.isdigit() and int(item_to_edit) <= len(todos):

                todos[int(item_to_edit) - 1] = input('Enter new todo: ') + "\n"
            elif item_to_edit in todos:
                new_value = input("Enter a new todo: ")
                found_item = todos.index(item_to_edit)
                todos[found_item] = new_value
            else:
                print("The todo with the provided name or number doesn't exist!")
        else:
            print("There is not item to edit. Please add an item")

        write_todo(todos)
    elif user_input.startswith("complete"):
        if todos:
            item_to_remove = int(user_input[9:]) or int(input("Enter the item you want to complete: "))

            if todos[item_to_remove - 1]:
                todos.pop(item_to_remove - 1)
                write_todo(todos)
    elif user_input.startswith('clear'):
        with open("file.txt", "w") as file:
            file.writelines("")
    elif "exit" in user_input:
        break
    else:
        print("Provided value doesn't exist in the todos list")


# contents = ["Content for docx.txt", "Content for reports.txt", "Content for presentation.txt"]
#
# filenames = ["docx.txt", "reports.txt", "presentation.txt"]
#
# for content, filename in zip(contents, filenames):
#     with open(f"files/{filename}", "w") as file:
#         file.writelines((content + "\n") * 10)

# member = input("Enter a member name: ") + "\n"
#
# with open("members.txt", "r") as file:
#     existing_members = file.readlines()
#
# existing_members.append(member)
#
# with open("members.txt", "w") as file:
#     file.writelines(existing_members)

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     with open(f"files/{filename}", "w") as file:
#         file.write("Hello")

# filenames = ["a.txt", "b.txt", "c.txt"]
#
# for filename in filenames:
#     with open(f"{filename}", "r") as file:
#         print(file.read())

# filenames = ["1.doc", "2.reports", "3.presentation"]
#
# new_filenames = [f.replace(".", "-") + ".txt" for f in filenames]
# print(new_filenames)

