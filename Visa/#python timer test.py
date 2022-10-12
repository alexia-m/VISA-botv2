import time
import datetime
 
# Create class that acts as a countdown
def countdown(m, s):
 
    # Calculate the total number of seconds
    total_seconds = 600
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
        
        if timer > 0:
            print("active")
        else:
            print ('not active')

 
 
    print("Bzzzt! The countdown is at zero seconds!")

    
 
# Inputs for hours, minutes, seconds on timer
m = 10
s = 0
countdown(int(m), int(s))