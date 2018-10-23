# print a message to the terminal window
print("Rules that govern the state of water")

# set up a variable to hold the temp we input
current_temp = False

while current_temp is False:
    # MAKE THIS A NUMBER!!
    x = current_temp
    current_temp = x
    # see what current temp is
    print("you input:", x)
    # if the current temp is at freezing or below, water is solid
    if (int(x) < 0 or (int(x) == 0)):
        print("water is a solid! cuz it be all froze and shit")
        x = False
    # else check another condition, if it's not freezing, is it below boiling?
    elif (int(x) < 100):
        print ("water is a liquid, cuz it ain't freezing or boiling")
        x = False

    elif (int(x) > 100 or (int(x) == 100)):
        print("water is a gas, cuz it be hot")
        x = False
