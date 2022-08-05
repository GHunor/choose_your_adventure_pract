#func greetings
#class scenerio
#func add scenerio

def greetings(GameName):
    print("Welcome to " + GameName +"!")

    playing = input("Do you want to play? ")
    if playing.lower() != "yes":
        print("k thx by!")
        quit()

# classes are overcomplicated|  functions building dictionaries or lists would be better
# but kept for practice
        
class s_option:
    def __init__(self, name, message, goal):
        self.name = name
        self.message = message
        self.goal = goal
        
class scenerio:
    biggest = [0,0]
    #index0: biggest one can go
    #index1: biggest exists
    
    def __init__(self, text):
        self.text = text
        #self.opt_num = 0
        self.opt_list = []
    def add_opt(self, opt):
        if isinstance(opt.goal,int):
            if opt.goal > self.biggest[0]:
                self.biggest[0] = opt.goal
        self.opt_list.append(opt)
    def add_opt_build(self, name, message, goal):
        self.add_opt(s_option(name, message, goal))
    def add_opt_list(self, OL):
        for i in OL:
            self.add_opt(i)
    def opt_num(self):
        return len(self.opt_list)
class whole:
      def __init__(self):
        self.scen_list = []
      def add_scen(self, scen):
        self.scen_list.append(scen)
        scen.biggest[1]=len(self.scen_list)
      def check_validity(self):
        if len(self.scen_list) == 0:
            return True
        elif self.scen_list[0].biggest[1] >= self.scen_list[0].biggest[0]:
            return True
        else:
            return False

def q_check(input):
    if input == "q":
        print("Bye!")
        quit()
def cycle(whole):
    sec = 0
    opt = 0
    print(whole.scen_list[0].text)
    while True:
        print("What do you want to do? Would you")


        for i in range(1,len(whole.scen_list[sec].opt_list)+1):
            if i > 1:
              print("OR")
            print(whole.scen_list[sec].opt_list[i-1].name + "(" + str(i) + ")")
        print("?")
        
        
        advn = input(">: ")
        q_check(advn.lower())
        if advn.isdigit() and int(advn) >= 1 and int(advn) <= whole.scen_list[sec].opt_num():
            opt = int(advn)-1
        else:
            print("Please give a valid option")
            continue
        print(whole.scen_list[sec].opt_list[opt].message)
        if whole.scen_list[sec].opt_list[opt].goal == "R":
            continue
        sec = whole.scen_list[sec].opt_list[opt].goal
        print(whole.scen_list[sec].text)
    
    
  


def main():
    greetings("Choose your own adventure")
    w = whole()
    w.add_scen(scenerio("You have entered a dungeon and you are presented with a lever and a door"))
    w.scen_list[0].add_opt_list([s_option("open the door", "The door is locked" ,"R"),
                                    s_option("pull the lever", "The door has opened and you entered through the door." ,1)])
    w.add_scen(scenerio("You are presented with a corridor going into the darkness with one door on each side"))
    w.scen_list[1].add_opt_list([s_option("open the door on the left", "The door is locked" ,"R"),
                                    s_option("open the door on the right", "You entered through the door." ,2),
                                    s_option("go further", "You venture deeper into the darkness, but you failed to realise there is a stair in front of you. You trip and fall down the stairs and die" ,-1)])
    w.add_scen(scenerio("You are presented with another door and a fountain"))
    w.scen_list[2].add_opt_list([s_option("drink from the fountain", "The water tastes funny" ,"R"),
                                    s_option("open the door", "You entered through the door and found a mountain of gold." ,-2)])
    w.add_scen(scenerio("You have won"))
    w.scen_list[3].add_opt(s_option("start over", "" ,0))
    w.add_scen(scenerio("You have died"))
    w.scen_list[4].add_opt(s_option("start over", "" ,0))                                
    cycle(w)
                                    
    
# Using the special variable 
# __name__
if __name__=="__main__":
    main()

        
'''
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
'''
