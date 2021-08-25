# # My solution

# game_state = True

# while game_state:
#     user_input = input(">").lower()

#     if user_input == "help":
#         print("start - to start the car")
#         print("stop - to stop the car")
#         print("quit - to exit")

#     elif user_input == "start":
#         print("Vroom, Vrooooom. Car Started... Ready to go!!")

#     elif user_input == "stop":
#         print("Car Stopped...")

#     elif user_input == "quit":
#         game_state = False
#         break

#     else:
#         print("I dont understand that!")

command = ""
started = False

while True:
    command = input("> ").lower()

    if command == "start":

        if started:
            print("CAR IS ALREADY STARTED!!")

        else:
            started = True
            print("Car Started...")

    elif command == "stop":

        if not started:
            print("CAR IS ALREADY STOPPED!!")

        else:
            started = False
            print("Car Stopped...")

    elif command == "help":
        print(
            """
start - to start the car
stop - to stop the car
quit - to quit
        """
        )

    elif command == "quit":
        break

    else:
        print("Sorry, I don't understand that")