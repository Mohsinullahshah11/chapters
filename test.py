filename = "learning_python.txt"

# Read the entire file
with open(filename) as file:
    contents = file.read()
print("=== Read entire file ===")
print(f'Content is {contents}')

# Loop over the file object
print("\n=== Loop over file object ===")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())