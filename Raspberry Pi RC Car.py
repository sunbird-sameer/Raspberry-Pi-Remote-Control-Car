import RPi.GPIO as GPIO
from time import sleep


in1 = 24
in2 = 23
en = 25

in3 = 17
in4 = 27
en2 = 22

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(en,GPIO.HIGH)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(en2,GPIO.HIGH)

p=GPIO.PWM(en,1000)
q=GPIO.PWM(en2,1000)

p.start(25)
q.start(25)

import time
import picamera


print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("0-stop w-forward s-backward a-left d-right 1-low 2-medium 3-high r-record")
print("\n")

while(1):
    
    x=raw_input()
    
    if x=='0':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
    
    
    elif x=='w':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
    
    
    
    elif x=='s':
        print("backward")
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
    
    elif x=='a':
        print("Left")
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
    
    elif x=='d':
        print("Right")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
    
    elif x=='1':
        print("low")
        p.ChangeDutyCycle(25)
        q.ChangeDutyCycle(25)
    
    
    elif x=='2':
        print("medium")
        p.ChangeDutyCycle(50)
        q.ChangeDutyCycle(50)
    
    
    elif x=='3':
        print("high")
        p.ChangeDutyCycle(100)
        q.ChangeDutyCycle(100)

    elif x=='r':
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.rotation=180
            camera.start_preview(fullscreen=False, window = (500, 100, 640, 480))
            time.sleep(2)
            camera.start_recording('/home/pi/Desktop/trialvideo.h264')
            time.sleep(5)
            camera.stop_recording()
            camera.stop_preview()


else:
    print("<<<  wrong data  >>>")
    print("please enter the defined data to continue.....")
