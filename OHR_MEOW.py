#Importing datetime to find current time
from datetime import datetime
def user_question(question):
    response = input(str(question)+" Y for yes   N or blank for no  ")
    if response.lower() == "y":
        return True
    else:
        return False
#Configs for use
hour_24 = user_question("Do you want 24 hour time?")
leading_0 = user_question("Do you want the leading zero before the hour?") #Changes leading 0 on hours 8 vs 08
display_seconds = user_question("Do you want to display seconds?")
if display_seconds:
    update_every_5_sec = user_question("Do you want to only update every 5 seconds instead of 1?")
else:
    update_every_5_sec = False
#Functions to be used later
def change_characters (input_str,to_change_from,to_change_to):
    output_str = ""
    for i in input_str:
        if str(i) == str(to_change_from):
            output_str = output_str + str(to_change_to)
        else:
            output_str = output_str + str(i)
    return output_str

def change_characters_list(input_list,to_change_from,to_change_to):
    output_list = []
    for i in input_list:
        output_list.append(change_characters(i,to_change_from,to_change_to))
    return output_list

def change_characters_2D_list(input_2D_list,to_change_from,to_change_to):
    output_2D_list = []
    for i in input_2D_list:
        output_2D_list.append(change_characters_list(i,to_change_from,to_change_to))
    return output_2D_list

def print_2D (in_list, space):
    for line in in_list:
        print(space+line)

#Cat Ascii Sprites for moving left and right
catL = [
    ">^.^< \\",
    "  mmmm/",
    " /\\  /\\"]

catR = [
    "/ >^.^<",
    "\\mmmm  ",
    "/\\  /\\ "]

#Ascii Numbers using a 7x6 grid
ascii0 = [
    " ##### ",
    "#     #",
    "#     #",
    "#     #",
    "#     #",
    " ##### "
]
ascii1 = [
    "  ##   ",
    " # #   ",
    "   #   ",
    "   #   ",
    "   #   ",
    "#######"
]
ascii2 = [
    " ##### ",
    "#     #",
    "      #",
    "   ### ",
    " ##    ",
    "#######"
]
ascii3 = [
    " ##### ",
    "#     #",
    "   ### ",
    "      #",
    "#     #",
    " ##### "
]
ascii4 = [
    "#     #",
    "#     #",
    "#######",
    "      #",
    "      #",
    "      #"
]
ascii5 = [
    "#######",
    "#      ",
    "###### ",
    "      #",
    "#     #",
    " ##### "
]
ascii6 = [
    " ######",
    "#      ",
    "###### ",
    "#     #",
    "#     #",
    " ##### "
]
ascii7 = [
    "#######",
    "      #",
    "    ## ",
    "  ##   ",
    " #     ",
    "#      "
]
ascii8 = [
    " ##### ",
    "#     #",
    " ##### ",
    "#     #",
    "#     #",
    " ##### "
]
ascii9 = [
    " ##### ",
    "#     #",
    " ######",
    "      #",
    "#     #",
    " ##### "
]
#Colon to be used to seperate hours and minutes
asciiColon = [
    " ",
    "#",
    " ",
    " ",
    "#",
    " "
]
#Null so I can add a blank character
ascii_null = [
    " "*0,
    " "*0,
    " "*0,
    " "*0,
    " "*0,
    " "*0
]
numbers = [ascii1,ascii2,ascii3,ascii4,ascii5,ascii6,ascii7,ascii8,ascii9,ascii0]
numbers = change_characters_2D_list(numbers,"#","&")

#Main Loop
time_first = datetime.now()
minute = time_first.minute
seconds = time_first.second
first_run = True
while True:
    time_first = datetime.now()
    if first_run:
        should_print = True
        first_run = False
    
    if not int(minute) == int(time_first.minute):
        should_print = True
    elif display_seconds and not round(int(seconds)) == round(int(time_first.second)):
        should_print = True
    if should_print and update_every_5_sec and not round(int(time_first.second))%5==0:
        should_print = False

    if should_print:
        should_print = False
        hour = time_first.hour
        minute = time_first.minute
        seconds = time_first.second
        if not hour_24:
            hour = hour%12

        minute=f"{minute:02}"
        hour=f"{hour:02}"
        seconds = f"{round(seconds):02}"
        
        num_1_int = int(hour[0])
        num_2_int = int(hour[1])
        num_3_int = int(minute[0])
        num_4_int = int(minute[1])

        num_5_int = int(seconds[0])
        num_6_int = int(seconds[1])

        if (num_1_int == 0) and not leading_0:
            num_1 = ascii_null
        else:
            num_1 = numbers[num_1_int-1]
        num_2 = numbers[num_2_int-1]
        num_3 = numbers[num_3_int-1]
        num_4 = numbers[num_4_int-1]

        num_5 = numbers[num_5_int-1]
        num_6 = numbers[num_6_int-1]
        
        lines_list = []
        for i in range(0,6):
            equals_before = "= "*15 
            if (num_1_int == 0) and not leading_0:
                after_space = "     "
            else:
                after_space = "  "
            line_text = equals_before+" "+num_1[i]+"  "+num_2[i]+"   "+asciiColon[i]+"   "+num_3[i]+"  "+num_4[i]
            if display_seconds:
                line_text = line_text +"   "+asciiColon[i]+"   "+num_5[i]+"  "+num_6[i] +" "
            line_text = line_text+after_space+equals_before
            lines_list.append(line_text)
        
        length = len(lines_list[1])
        lenth_filled = ("= ")*(round((length/2)+0.1))
        multiplier_spaces = round((length-10)/30)
        if int(minute)<30:
            cat = catR
            spaces = ((int(minute)%30*multiplier_spaces))
        else:
            cat = catL
            spaces = (length-7)-(int(minute)%30*multiplier_spaces)
        spacing = " "*spaces
        for line in cat:
            print(spacing+line)
        print(lenth_filled)
        print_2D(lines_list,"")
        print(lenth_filled)