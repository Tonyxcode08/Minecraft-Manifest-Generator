#Input Handling
running = True

#Default Values
name = "my mod"
description = "my modpack"
min_engine_version = [1, 20, 0]
datatype = "data"

#Version list
version = [1, 0, 0]

#Prints everything
def print_all():
    print("\n")
    print(name)
    print(description)
    print(version)
    print(min_engine_version)
    print(datatype)

#Appends all the versions to the list
def version_append_all():
    version.append(version_major)
    version.append(version_minor)
    version.append(version_patch)

#Main Loop
while running:
    choice = int(input("What would you like to edit? \n 0. Quit \n 1. Name \n 2. Description \n 3. Version \n 4. Min Engine Version \n 5. Type \n \n "))
    match choice:
        case 0:
            print_all()
            break
            
        case 1:
            name = input(str("What is the name of your modpack? \n"))
            continue
        case 2:
            description = input(str("Please enter the decription of your mod \n"))
            continue
        case 3:
            version.clear()
            version_major = int(input("What is the major version of your mod? \n"))
            version_minor = int(input("What is the minor version of your mod? \n"))
            version_patch = int(input("What is the patch number of your mod? \n"))
            version_append_all()
            continue
        case 4:
            min_engine_version = str(input("What is your desired min engine version? \n (Please separate numbers using commas) \n "))
            min_engine_version.split(",")
            continue
        case 5:
            datatype = str(input("What datatype would you like the pack to be? \n Options: \n data \n resources \n script \n world_template \n skin_pack \n "))
            continue