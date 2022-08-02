#func greetings
#class scenerio
#func add scenerio

def greetings(GameName):
    print("Welcome to")

    playing = input("Do you want to play? ")
    if playing.lower() != "yes":
        print("k thx by!")
        quit()

def main():
    print("Choose your own adventure!")

    playing = input("Do you want to play? ")
    if playing.lower() != "yes":
        print("k thx by!")
        quit()
    #maybe class would be better than dictionary
    scenerio1 = {
        "text": "You have entered a dungeon and you are presented with a lever and a door",
        "option_num": 2,
        "option_1": "open the door",
        "option_1M": "The door is locked",
        "option_1G": "R",
        "option_2": "pull the lever",
        "option_2M": "The door has opened and you entered through the door.",
        "option_2G": 1 }
    scenerio2 = {
        "text": "You are presented with a corridor going into the darkness with one door on each side",
        "option_num": 3,
        "option_1": "open the door on the left",
        "option_1M": "The door is locked",
        "option_1G": "R",
        "option_2": "open the door on the right",
        "option_2M": "You entered through the door.",
        "option_2G": 2,
        "option_3": "go further",
        "option_3M": "You venture deeper into the darkness, but you failed to realise there is a stair in front of you. You trip and fall down the stairs and die",
        "option_3G": -1,
        }
    scenerio3 = {
        "text": "You are presented with another door and a fountain",
        "option_num": 2,
        "option_1": "drink from the fountain",
        "option_1M": "The water tastes funny",
        "option_1G": "R",
        "option_2": "open the door",
        "option_2M": "You entered through the door and found a mountain of gold.",
        "option_2G": -2 }

    LOS = [scenerio1,scenerio2,scenerio3]
    Special = ["You died", "You win"]

    sec = 0
    opt = 0
    print("q for exit")
    print(LOS[sec]["text"])

    while True:
        
        print("What do you want to do? Would you")
        for i in range(1,LOS[sec]["option_num"]+1):
            if i > 1:
              print("OR")
            print(LOS[sec]["option_" + str(i)] + "(" + str(i) + ")")
        print("?")
        
        
        advn = input(">: ")
        if advn.isdigit() and int(advn) >= 1 and int(advn) <= LOS[sec]["option_num"]:
            opt = int(advn)
        elif advn.lower() == "q":
            print("Bye!")
            quit()
        else:
            print("Please give a valid option")
            continue
        if LOS[sec]["option_" + str(opt) + "G"] in [-1,-2]:
            print(Special[LOS[sec]["option_" + str(i) + "G"]*-1-1])
            quit()
        print(LOS[sec]["option_" + str(opt) + "M"])
        if LOS[sec]["option_" + str(opt) + "G"] == "R":
            continue
        sec = LOS[sec]["option_" + str(opt) + "G"]
        
        print(LOS[sec]["text"])

# Using the special variable 
# __name__
if __name__=="__main__":
    main()

