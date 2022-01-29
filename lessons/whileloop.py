"""An example of a while loop statement"""

counter: int = 0
maximum: int = int(input("Count up to, but not including what?"))
while counter < maximum:
    counter_squared: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1  # This is necessary in order to prevent the computer from typing the same loop repeated. Will continue to do this until process is stopped or computer is shut down. This is called an infinite loop. 

print("Done!")