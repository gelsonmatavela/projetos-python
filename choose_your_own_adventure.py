name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("Your are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross.  ").lower()
    
    if answer == "swim":
        print("You swim accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, run out of water and you lost the game! ")
    else:
        print("Not a valid option. You lose.")
        
elif answer == "right":
    print("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        print("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        
        if answer == "yes":
            print("You talk to the stranger and give you GOLD. You win! Congractulations.")
        elif answer == "no":
            print("You ignored the stranger and they are offended an you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
    
else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name)