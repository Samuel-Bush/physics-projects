import math # Allows for use of cosine and sine functions

y = 0 # Y must be established before while loop as it is included in the condition (x does not need to be established before)
time = 0
speed = int(input("Enter launch speed (m/s): "))
angle = int(input("Enter launch angle (deg): "))
radians = math.radians(angle) # Python sin and cos accept values in radian so conversion is needed

while y >=  0: # So the co-ordinates stop outputting when projectile hits the 'ground'
  x = speed * math.cos(radians) * time # Calculate with general equation for x co-ordinate of projectile
  y = speed * math.sin(radians) * time - (0.5 * 9.8 * time**2) # Calculate with general equation for y co-ordinate of projectile
  print(f"[{x},{y}]")
  time = time + 0.2 # Co-ordinate output interval is 0.2s to balance detail needed and amount of outputs
