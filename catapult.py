from hub import button, light_matrix
import runloop
import motor
import time
from hub import port

def clasp():
    print("clasp paper ball")
    motor.run_for_degrees(port.F, 720, 720) 
    time.sleep(2) 

def clasp_release():
    print("Releasing clasp and retreat")
    motor.run_for_degrees(port.F, -540, 720)
    time.sleep(2)

def drop():
    print("drop ball onto catapult")
    motor.run_for_degrees(port.D, -77, 20)
    time.sleep(4)

def retreat():
    print("drop ball onto catapult")
    motor.run_for_degrees(port.D, 76, 20)
    time.sleep(4)

def throw():
    print("Throw ball onto bucket")
    motor.run_for_degrees(port.B, 540 , 540)
    time.sleep(4)

def reset_throw():
    print("Reset state for next throw")
    motor.run_for_degrees(port.B, -540, 540)
    time.sleep(4)




def main():
    while (1) :
        if button.pressed(button.RIGHT):
            clasp()
            drop()
            clasp_release()
            retreat()
            throw()
            reset_throw()
            break

while True:
    if __name__ == "__main__":
        main()
