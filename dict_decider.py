import random as r

full_dict = {
    "Thighs" : ["girl on her knees","fishnets","skirt","face",
                "pair of thigh highs","selfie","\"sfw\" image","exposed midriff",
                "exposed panties","cleavage","naked ass","fully nude girl",
                "pussy","butt cheek","exposed nipple","solo image","thigh"],
    "thighdeology" : ["thigh/butt being squeezed","topless girl","cameltoe",
                      "pair of thigh highs","garter","skirt","exposed panties",
                      "exposed midriff","\"sfw\" image","exposed boobs","bikini",
                      "ass","solo image","thigh"]
}

def roll(sub):
    x = r.randint(1,10)
    y = r.randint(1,len(full_dict[sub])-2)
    z = r.randint(1,10)
    return x,y,z
def z_mods(x,y,z,score,sub,mode,dif):
    end = False
    mod_x = x
    mod_y = y
    if z <=3:
        mod_x += z
    elif z <= 6:
        mod_y += (z - 3)
    elif z <= 7:
        mod_x = r.randint(x+1,15)
    elif z <= 8:
        mod_x = 10
        mod_y = len(full_dict[sub])-2
    elif z <= 10:
        z_2 = r.randint(1,10)
        if z_2 <= 2:
            if score >= (450 // dif) and mode == 1:
                end = True
            else:
                mod_x += (z_2 + 3)
        elif z_2 <= 4:
            if score >= (450 // dif) and mode == 1:
                end = True
            else:
                mod_y += (z_2 + 1)
        elif z_2 <= 7:
            if score >= (360 // dif) and mode == 1:
                end = True
            else:
                mod_x += (z_2 - 2)
                mod_y += (z_2 - 2)
        elif z_2 <= 8:
            if score >= (270 // dif) and mode == 1:
                end = True
            else:
                mod_x = 14
                mod_y = len(full_dict[sub])+2
        elif z_2 <= 9:
            if score >= (180 // dif) and mode == 1:
                end = True
            else:
                mod_x = 14
                mod_y = len(full_dict[sub])+2
        elif z_2 <= 10:
            if score >= (90 // dif) and mode == 1:
                end = True
            else:
                mod_x = 15 
                mod_y = len(full_dict[sub])+3
    if score > (1020 // dif) and mode == 1:
        end = True
    return mod_x,mod_y,end
def x_num(x):
    if x <= 7:
        return ((x+1)*5) + r.randint(0,4)
    elif x <= 10:
        return r.randint(51,100)
    elif x <= 13:
        return r.randint(101,150)
    elif x <= 15:
        return r.randint(151,200)
def y_trig(y,sub):
    if y <= len(full_dict[sub]):
        trig = "\033[93m" + full_dict[sub][y-1] + "\033[0m"
    elif y <= len(full_dict[sub])+3:
        trig = "\033[93m" + full_dict[sub][len(full_dict[sub])-(y-len(full_dict[sub]))] + "\033[0m" + " and each " + "\033[93m" + full_dict[sub][r.randint(y-len(full_dict[sub]),len(full_dict[sub])-2)] + "\033[0m"
    return trig

def grab_dif(dif=""):
    dif = input("Enter 1,2,3 for easy, medium, or hard difficulty: ")
    if dif != "1" and dif != "2" and dif != "3":
        dif = grab_dif()
    return dif
def grab_mode(mode=""):
    mode = input("Enter \"1\" for random game length or \"2\" for high score mode: ")
    if mode != "1" and mode != "2":
        mode = grab_mode()
    return mode
def grab_round_end(round_end=""):
    round_end = input("Press enter to continue, or \"X\" to stop and view your final score: ")
    if round_end != "" and round_end != "X" and round_end != "x":
        round_end = grab_round_end()
    return round_end

def repeat_modes(mode,dif):
    end = False
    score = 0
    while end == False:
        sub = list(full_dict.keys())[r.randrange(0,len(full_dict))]
        x, y, z = roll(sub)
        x, y, end = z_mods(x,y,z,score,sub,mode,dif)
        num = x_num(x) // dif
        round_score = 1 + (num // (15 // dif)) + int(((y / len(full_dict[sub])) * num) / (20 // dif))
        score += round_score
        trig = y_trig(y,sub)
        print()
        print("Go to https://www.reddit.com/r/" + "\033[94m" + sub + "\033[0m")
        print("Look at the next" + "\033[91m" , num , "\033[0m" + "posts.")
        print("Edge once for each " + trig + ".")
        print("Round score:",round_score,end = "")
        if round_score > 20 and dif == 1:
            print(", good luck!")
        else:
            print("")

        if end == False and mode == 1:
            input("Press enter to continue.")
            continue
        elif end == True and mode == 1:
            input("You are free, press enter to end.") 
            print("Final score:",score)

        if mode == 2:
            round_end = grab_round_end()
            if round_end == "":
                continue
            else:
                end = True
                print("Final score:",score)

def main():
    repeat_modes(int(grab_mode()),4-int(grab_dif()))

main()