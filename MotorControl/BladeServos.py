#!/usr/bin/python
import time

import Jetson.GPIO as GPIO
#import RPi.GPIO as GPIO
from PCA9685_Servo import PCA9685

# try:
#print "This is an PCA9685 routine"
pwm = PCA9685()
pwm.setPWMFreq(50)
#pwm.setServoPulse(1,500) 
channelnum=2

pwm.setRotationAngle(channelnum, 90)

while True:
    #setServoPulse(2,2500)
    for i in range(40,170,1): 
        pwm.setRotationAngle(channelnum, i)   
        time.sleep(0.025)

    for i in range(170,40,-1): 
        pwm.setRotationAngle(channelnum, i)   
        time.sleep(0.025)
    
    
    
    # works to move blade
    # for i in range(40,140,1): 
    #     pwm.setRotationAngle(1, i)   
    #     time.sleep(0.025)

    # for i in range(140,40,-1): 
    #     pwm.setRotationAngle(1, i)   
    #     time.sleep(0.025)
    
    
    
    # test moves to specific angles
    # pwm.setRotationAngle(1, 90) 
    # time.sleep(10)
    # pwm.setRotationAngle(1, 40) 
    # time.sleep(5)
    # pwm.setRotationAngle(1, 140) 
    # time.sleep(5)




# except:
    # pwm.exit_PCA9685()
    # GPIO.cleanup()
    # print "\nProgram end"
    # exit()