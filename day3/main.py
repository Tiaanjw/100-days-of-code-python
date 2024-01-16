print("Welcome to babylon, you arrive by boat.")
print("A strange man greats you as you step onto the docks for the first time.")

c1 = input("G'day sir, I have some fresh water, do you want a sip? yes or no?\n")
if c1 == "yes":
  print("The water contained some sort of poison and you immediately pass out, you lose.")

else: 
  print("Your gut tells you to take nothing from this strange man and you continue walking past him.")

  c2 = input("On your way to the castle you encounter a fork in the road, which path do you take, the one on the left, or the one on the right?")
  if c2 == "left":
    print("It seems to be the right path and you continue walking")
    print("You pass by some stables with beautifull horses, you considder buying one.")

    c3 = input("there are three horses, a black, brown and white one. Which horse do you chose?")
    if c3 == "black":
      print("As you mount the horse, it suddenly became agitated and throws you to the ground, you hit your head on a rock and pass out, you lose")
    
    elif c3 == "brown":
      print("At first the horse didnt seem to mind you, but sudddenly it started running with you on its back, faster and faster, you fell off and break your legs, you can no longer get to the castle, you lose.")
    
    else:
      print("The white horse looks you in the eye, you mount it without issues, it already knows the way to the castle")
      print("after 2 days and 2 nights, you reach the castle to meet the king, game over, you win!")

  else:
    print("After taking the path on the right, you walk into a dense forrest, you are starting to become worried")
    print("Suddenly the strange man from the docks leaps from behind a tree and knocks you on the head with a broom, you hit the floor and pass out, you lose.")

