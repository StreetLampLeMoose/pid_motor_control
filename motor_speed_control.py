import machine
#this works quite well

def motor_speed_control (speed, pin_EN, pin_1A, pin_2A, direction ,stop=False):
    pinEn = machine.PWM(machine.Pin(pin_EN))
    pin1A = machine.Pin(pin_1A, machine.Pin.OUT)
    pin2A = machine.Pin(pin_2A, machine.Pin.OUT)
    
    if stop:
        pin1A.low()
        pin2A.low()
        return
    
    if direction == 1:
        pin1A.high()
        pin2A.low()
    elif direction == 0:
        pin1A.low()
        pin2A.high()
        
    pinEn.freq(60)
    pinEn.duty_u16(speed)
    
    return