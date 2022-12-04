import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(2,IO.OUT) 
IO.setup(3,IO.OUT) 
IO.setup(14,IO.IN) 
while 1:
    if(IO.input(14)==True): 
        IO.output(2,True) 
        IO.output(3,False) 
    if(IO.input(14)==False): 
        IO.output(3,True) 
        IO.output(2,False) 
 
