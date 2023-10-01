#Escape maze in the Reeborg's World

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#trying to get to a wall in case of an infinite loop
while front_is_clear():
    move()

 #locating a wall
turn_left()

#As long as we are not at goal
while not at_goal():
    #the aim is to move the robot to the right as much as we can
    if right_is_clear():
        turn_right()
        move()

    #If we can't move the robot to the right then we should move
    elif front_is_clear():
        move()

    #Otherwise turn left to go to the goal
    else:
        turn_left()

    else:
        turn_left()