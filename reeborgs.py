#huddle-1:
===========
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def movement():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range(6):
   movement()
   
   #huddle-2:
   def turn_right():
       turn_left()
        turn_left()
         turn_left()
    def bypasswall():
        move()
         turn_left()
         move()
         turn_right()
         move()
         turn_right()
         move()
         turn_left()  
     while at_goal()==false:
         bypasswall()       
   
   #huddle-3:
===========
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def movement():
    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not(at_goal()):
    if wall_in_front():
        movement()
    else:
        move()
        
        #huddle-4:
===========
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def robote():
   turn_left()
    move()
    while (wall_on_right()):
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not(at_goal()):
    if wall_in_front():
        robote()
    else:
        move()