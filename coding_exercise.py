new_member = input("Add a new member:")
with open("members.txt", "w") as file:
    file.write(new_member)

file.close()
