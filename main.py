with open("./Input/Names/invited_names.txt", mode="r") as names:
    list_of_names = names.read().split()

with open("./Input/Letters/starting_letter.txt") as starting:
    starting_letter = starting.read()
    for x in list_of_names:
        ready_letter = starting_letter.replace("[name]", x)

        with open(f"./Output/ReadyToSend/letter to {x}", "w") as ready:  # here with writ  method I am making new txt
            # files
            ready.write(f"{ready_letter}")
