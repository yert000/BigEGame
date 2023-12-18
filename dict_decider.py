import random as r

full_dict = {
    "Thighs" : 
    ["girl on her knees","fishnets","skirt","face",             #
    "pair of thigh highs","selfie","\"sfw\" image",
    "exposed midriff","exposed panties","cleavage","naked ass",
    "fully nude girl","pussy","butt cheek","exposed nipple",
    "solo image","thigh"],

    "thighdeology" : 
    ["thigh/butt being squeezed","topless girl",
    "cameltoe","pair of thigh highs","garter","skirt",
    "exposed panties","exposed midriff","\"sfw\" image",
    "exposed boobs","bikini","ass","solo image","thigh"],

    "ClothedForPrejacs" : 
    ["girl with tattoo","cameltoe","underboob","underbutt",
    "cleavage","fully clothed girl","ass in panties","midriff",
    "girl in underwear","face","foot","\"sfw\" image"],

    "facial" : 
    ["fully naked girl","fully clothed girl","necklace/choker",
    "dick in mouth","girl with glasses","girl with tongue out",
    "girl with multiple loads","cum shot","dick","boobs",
    "girl on knees","cum on chest","cum in mouth",
    "cum on face"],

    "cumsluts" : 
    ["fully clothed girl","girl with multiple loads","creampie",
    "dick in mouth","cum on ass","cum on chest","dick",
    "pussy","ass","cum in mouth","cumshot","cum on body",
    "girl with tongue out","girl on knees","cum on face","face",
    "image with cum"],

    "petite" : 
    ["fully clothed girl","bikini","girl masturbating",
    "girl on her knees","selfie","girl with tattoo","ass",
    "\"sfw\" image","pussy","midriff","boobs","face","cleavage",
    "girl in underwear","foot","fully nude girl","solo image"],

    "midriff" :
    ["naval piercing","image in public","ass","selfie",
    "\"nsfw\" image","girl with abs","bikini","skirt",
    "girl on knees","fully clothed girl","tatto","face",
    "girl in underwear","cleavage","\"sfw\" image","midriff"],

    "lesbians" :
    ["face sitting","fingering","couple making out",
    "group of 3+","strap-on","dildo","scissoring","boobs","ass",
    "pussy","belly button","foot","fully nude girl",
    "cunnilingus","nipple","lesbian"],

    "PristineGirls" :
    ["girl with jewelry","image with 2+ girls","outdoor image",
    "partially clothed girl","full body shot","wet/oiled girl",
    "eye contact","ass","boobs","pussy","belly button","foot",
    "nipple","fully nude girl"],

    "sexygirls" :
    ["full body shot","dress","girl on knees",
    "nipple through shirt","ass","midriff","cleavage","bikini",
    "eye contact","image in public","selfie",
    "girl in underwear","fully clothed girl","face",
    "\"sfw\" image"],

    "GodPussy" :
    ["buttplug","girl with tatto","girl with top on",
    "full body shot","underwear pushed to side","selfie",
    "eye contact","girl touching pussy","girl on back",
    "girl on knees","legs together","fully nude girl","face",
    "foot","belly button","boobs","legs spread","ass",
    "butthole","pussy"],

    "EGirls" :
    ["gaming chair","ahegao face","fully clothed girl",
    "cosplay","girl with tattoo","colored hair","fake ears",
    "selfie","fully nude girl","goth girl","ass","pussy",
    "midriff","boobs","face","cleavage","thigh highs",
    "girl in underwear","egirl"],

    "AsiansGoneWild" :
    ["fully clothed girl","bikini","girl masturbating",
    "\"sfw\" image","girl on her knees","selfie",
    "girl with tattoo","ass","pussy","midriff","boobs","face",
    "cleavage","girl in underwear","foot","fully nude girl",
    "solo image"],

    "public" :
    ["couple having sex","girl masturbating","blowjob",
    "skirt lift","shirt/bra lift","pants/panties pulled down",
    "bathroom","store","beach","forest","bottomless","topless",
    "fully nude girl","outdoor image","pussy","ass","boobs",
    "girl"],

    "Bikini" :
    ["nipple","full body shot","eye contact","selfie","foot",
    "underboob","girl in water","\"nsfw\" image","beach","ass",
    "midriff","cleavage","girl not in a bikini","face",
    "bikini"],

    "hentai" :
    ["schoolgirl outfit","futanari","footjob","boobjob",
    "cunnilingus","fingering","group image","blowjob",
    "penetrative sex","fully clothed girl","solo image","dick",
    "foot","pussy","ass","boobs","fully nude girl","girl"],

    "rule34" :
    ["futanari","footjob","boobjob","cunnilingus","fingering",
    "irl cosplay","group image","3D render","blowjob",
    "penetrative sex","fully clothed girl","solo image","dick",
    "foot","pussy","ass","boobs","fully nude girl","girl",
    "character you recognize",],

    "FemboyHentai" :
    ["female","chastity cage","catboy","fully clothed femboy",
    "creampie","thigh highs","fishtail","bulge","blowjob",
    "femboy masturbating","anal sex","cum","boy pussy","ass",
    "dick"],

    "FemBoys" :
    ["chastity cage","fully clothed femboy","femboy with boobs",
    "thigh highs","femboy on knees","femboy stroking","foot",
    "anal","spread cheeks","skirt","panties","cum","bulge",
    "solo image","boy pussy","ass","dick"],
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
        if round_score > 23 and dif == 1:
            print(", good luck!")
        else:
            print("")

        if end == False and mode == 1:
            input("Press enter to continue.")
            continue
        elif end == True and mode == 1:
            input("You are free! Press enter to end.") 
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