import os

while True:
    cwd = str(input("Please paste the path to the desired directory here: \n "))
    choice = str(input("Is this the correct directory? Y/N "))
    if choice.lower() == "y":
        os.chdir(cwd)
        with open("ExampleFile.txt", "w") as file:
            file.write("Hello, World!")
            print(f"a file has been made in {cwd}")
            break
    elif choice.lower == "n":
        continue
    else:
        break

