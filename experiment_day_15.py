import glob

my_files = glob.glob("files/*.txt")

for filepath in my_files:
    with open(filepath, 'r') as file:
        print(file.read())
