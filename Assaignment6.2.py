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

ROUTE_FILE = "route.txt"

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

# Command name in file -> function
COMMANDS = {
    "FORWARD": move_forward,
    "BACKWARD": move_backward,
    "LEFT": turn_left,
    "RIGHT": turn_right,
    "AROUND": turn_around,
}

def read_route(filename):
    """Read movement instructions from a file, one command per line."""
    route = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip().upper()
            if line == "" or line.startswith("#"):
                continue  # skip empty lines and comments
            route.append(line)
    return route

def run_route(route):
    for command in route:
        if command in COMMANDS:
            print("Doing:", command)
            COMMANDS[command]()
        else:
            print("Unknown command, skipping:", command)

try:
    stop()
    route = read_route(ROUTE_FILE)
    print("Route loaded:", route)
    sleep(5)  # time to put the car down
    run_route(route)
except OSError:
    print("Could not open", ROUTE_FILE)
finally:
    stop()