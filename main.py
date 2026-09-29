from machine import Pin, PWM
from time import sleep

# FoCar motor pins
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

e1.freq(1000)
e2.freq(1000)

SPEED = 32767
HALF_METER_TIME = 2.0
TURN_90_TIME = 0.8


def stop():
    e1.duty_u16(0)
    e2.duty_u16(0)


def run_motors():
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)


def move_forward():
    m1.value(1)
    m2.value(1)
    run_motors()
    sleep(HALF_METER_TIME)
    stop()
    sleep(1)


def move_backward():
    m1.value(0)
    m2.value(0)
    run_motors()
    sleep(HALF_METER_TIME)
    stop()
    sleep(1)


def turn_left():
    m1.value(0)
    m2.value(1)
    run_motors()
    sleep(TURN_90_TIME)
    stop()
    sleep(1)


def turn_right():
    m1.value(1)
    m2.value(0)
    run_motors()
    sleep(TURN_90_TIME)
    stop()
    sleep(1)


def turn_around():
    m1.value(0)
    m2.value(1)
    run_motors()
    sleep(TURN_90_TIME * 2)
    stop()
    sleep(1)


try:
    stop()
    sleep(5)

    move_forward()
    turn_left()
    move_forward()
    turn_left()
    move_forward()
    turn_right()
    move_forward()
    turn_right()
    move_forward()
    turn_around()
    move_backward()

finally:
    stop()