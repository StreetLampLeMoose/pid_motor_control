import machine
import time
#this works pretty well

def get_distance(trigger_Pin,echo_Pin) :
    triggerPin = machine.Pin(trigger_Pin,machine.Pin.OUT)
    echoPin = machine.Pin(echo_Pin,machine.Pin.IN,machine.Pin.PULL_DOWN)
    triggerPin.value(0)
    time.sleep_us(5)
    triggerPin.value(1)
    time.sleep_us(10)
    triggerPin.value(0)
    timePassed = machine.time_pulse_us(echoPin,1,30000)
    if timePassed >= 23323 or timePassed < 0 :
        print("max distance measured")
        return 400
    distance = (timePassed *0.0343) / 2
    print("distance : " , distance , "cm")
    return distance

