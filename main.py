from machine import Pin
from time import sleep


ledPin = Pin(25, Pin.OUT)
msPin = Pin(27, Pin.IN)


def isMotionDetected():
    if msPin.value() == 1:
        return True

    return False


def activateEyes():
    if isMotionDetected():
        print("Motion Detected!")
        ledPin.value(1)


def main():
    # PIR initialization period
    sleep(60)

    print("Sleep Done")
    print("Initiating Program ...")

    while True:
        activateEyes()
main()
