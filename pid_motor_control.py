from get_distance import get_distance
from motor_speed_control import motor_speed_control
import time
k = 1
ki = 1
kd = 1
maxIntegral = ((1/2) / 2)*(23323)
maxDerivative = (1/2) /(23323)
maxOutput = k*(1/2) + kd*maxDerivative + ki * maxIntegral

while True:
    startTime = time.ticks_us()
    distance = get_distance(14,15)
    endTime = time.ticks_us()
    integral = ((distance) / 2)*(endTime - startTime)
    derivative = (distance) /(endTime - startTime)
    pidOutput = k*(distance) + kd*derivative + ki * integral
    
    motor_speed_control(int(pidOutput),18,17,16,1)
    