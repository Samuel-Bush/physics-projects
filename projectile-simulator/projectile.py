import math # Allows for use of cosine and sine functions

y = 0 # Y must be established before while loop as it is included in the condition (x does not need to be established before)
time = 0
speed = int(input("Enter launch speed (m/s): "))
angle = int(input("Enter launch angle (deg): "))
timeInterval = float(input("Enter position output interval (s, generally 0.01 - 1): ")
radians = math.radians(angle) # Python sin and cos accept values in radian so conversion is needed

while y >=  0: # So the co-ordinates stop outputting when projectile hits the 'ground'
  x = speed * math.cos(radians) * time # Calculate with general equation for x co-ordinate of projectile
  y = speed * math.sin(radians) * time - (0.5 * 9.8 * time**2) # Calculate with general equation for y co-ordinate of projectile
  print(f"[{round(x,2)},{round(y,2)}]")
  time = time + timeInterval # Co-ordinate output interval is dertemined by user input on line 7
