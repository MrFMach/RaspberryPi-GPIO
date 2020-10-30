import RPi.GPIO as gpio
import time
# All code in the try block for error handling
try:    
    # Disable GPIO warnings
    gpio.setwarnings(False)
    # Pins board reference (1-40)
    gpio.setmode(gpio.BOARD)
    # Set output
    gpio.setup(23, gpio.OUT, initial=gpio.LOW)
    gpio.setup(31, gpio.OUT, initial=gpio.LOW)
    gpio.setup(33, gpio.OUT, initial=gpio.LOW)
    gpio.setup(35, gpio.OUT, initial=gpio.LOW)
    gpio.setup(37, gpio.OUT, initial=gpio.LOW)
    # Set input
    gpio.setup(3, gpio.IN)
    gpio.setup(5, gpio.IN)
    gpio.setup(7, gpio.IN)
    
    # Started signal
    gpio.output(23, 1)
    
    while 1:

        if gpio.input(3) == False:
            print("Button-3 pressed, blinking Led-33")
            gpio.output(33, 1)
            time.sleep(0.1)
            gpio.output(33, 0)
            time.sleep(0.1)

        elif gpio.input(5) == False:
            print("Button-5 pressed, blinking Led-37")
            gpio.output(37, 1)
            time.sleep(0.1)
            gpio.output(37, 0)
            time.sleep(0.1)
     
        elif gpio.input(7) == False:
            print("Button-7 pressed, blinking Led-35")
            gpio.output(35, 1)
            time.sleep(0.1)
            gpio.output(35, 0)
            time.sleep(0.1)
        else:
            print("No button pressed")
            print("-press any button or type Ctrl+C to exit\n")
            gpio.output(31, 1)
            time.sleep(0.3)
            gpio.output(31, 0)
            time.sleep(0.5)

# If you press Ctrl+C, execute what is in 'except' and go to 'finally'
except KeyboardInterrupt:    
    print ("\nYou left the program")    
finally:
    print ("Cleaning up GPIO...")
    gpio.cleanup()
    print ("Bye!")
