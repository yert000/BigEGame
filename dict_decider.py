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

def z_mods(x,y,z,score):
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
        mod_y = 10
    elif z <= 10:
        z_2 = r.randint(1,10)
        if z_2 <= 2:
            mod_x += (z_2 + 3)
        elif z_2 <= 4:
            mod_y += (z_2 + 1)
        elif z_2 <= 7:
            mod_x += (z_2 - 2)
            mod_y += (z_2 - 2)
        elif z_2 <= 8:
            mod_x = 14
            mod_y = 14
        elif z_2 <= 9:
            if score >= 100:
                end = True
            else:
                mod_x = 14
                mod_y = 14
        elif z_2 <= 10:
            if score >= 50:
                end = True
            else:               # bad ending
                mod_x = 15 
                mod_y = 15
    return mod_x,mod_y,end

def x_num(x):
    if x <= 7:
        return ((x+1)*5) + r.randint(1,4) , False
    elif x <= 10:
        return r.randint(51,100) , False
    elif x <= 13:
        return r.randint(101,150) , False
    elif x <= 14:
        return r.randint(151,200) , False
    elif x <= 15:
        return r.randint(1,200) , True
    
def y_trig(y,sub):
    if y <= len(full_dict[sub]):
        trig = "\033[93m" + full_dict[sub][y-1] + "\033[0m"
    elif y <= len(full_dict[sub])+3:
        trig = "\033[93m" + full_dict[sub][len(full_dict[sub])-(y-len(full_dict[sub]))] + "\033[0m" + " and each " + "\033[93m" + full_dict[sub][r.randint(y-len(full_dict[sub]),len(full_dict[sub])-2)] + "\033[0m"
    return trig

def main():
    end = False
    score = 0
    while end == False:
        sub = list(full_dict.keys())[r.randrange(0,len(full_dict))]
        x, y, z = roll(sub)
        extra_x = False
        x, y, end = z_mods(x,y,z,score)
        num, extra_x = x_num(x)
        round_score = 1 + int(num * (y / len(full_dict[sub])))//20
        score += round_score
        trig = y_trig(y,sub)
        print()
        print("Go to https://www.reddit.com/r/" + "\033[94m" + sub + "\033[0m")
        print("Look at the next" + "\033[91m" , num , "\033[0m" + "posts.")
        print("Edge once for each " + trig + ".")
        print("Difficulty: " + str(round_score) + "/10",end="")
        if round_score > 10:
            print(", good luck!")
        else:
            print("")
        if extra_x == True:
            print("Every time you edge add 1 more post to the total amount.")
        if end == False:
            input("Press enter to continue.")
        else:
            input("You are free, press enter to end.") 
            print("Final score:",score)

main()