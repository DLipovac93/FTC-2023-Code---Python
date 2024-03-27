myVariable = 0

def when_started1():
    global myVariable
    arm_Pos.set_velocity(10, PERCENT)
    arm_Pos.set_position(0, DEGREES)
    Claw.set_position(0, DEGREES)
    Plane_feed.set_position(0, DEGREES)
    plane_launch.set_velocity(100, PERCENT)
    Plane_feed.set_velocity(25, PERCENT)
    plane_launch.set_velocity(100, PERCENT)
    plane_launch.set_velocity(100, PERCENT)

def onevent_controller_1buttonX_pressed_0():
    global myVariable
    arm_Pos.spin_to_position(15, DEGREES)

def onevent_controller_1buttonA_pressed_0():
    global myVariable
    arm_Pos.spin_to_position(7.5, DEGREES)

def onevent_controller_1buttonB_pressed_0():
    global myVariable
    arm_Pos.spin_to_position(0, DEGREES)

def onevent_controller_1buttonY_pressed_0():
    global myVariable
    arm_Pos.spin_to_position(45, DEGREES)

def onevent_controller_1buttonUp_pressed_0():
    global myVariable
    plane_launch.spin(FORWARD)
    wait(3, SECONDS)
    plane_launch.stop()

def onevent_controller_1buttonL1_pressed_0():
    global myVariable
    Claw.spin_to_position(90, DEGREES)

def onevent_controller_1buttonR1_pressed_0():
    global myVariable
    Claw.spin(REVERSE)

def onevent_controller_1buttonR1_released_0():
    global myVariable
    Claw.set_position(0, DEGREES)
    Claw.stop()

def onevent_controller_1buttonDown_pressed_0():
    global myVariable
    Plane_feed.spin_for(FORWARD, 90, DEGREES)

# system event handlers
controller_1.buttonX.pressed(onevent_controller_1buttonX_pressed_0)
controller_1.buttonA.pressed(onevent_controller_1buttonA_pressed_0)
controller_1.buttonB.pressed(onevent_controller_1buttonB_pressed_0)
controller_1.buttonY.pressed(onevent_controller_1buttonY_pressed_0)
controller_1.buttonUp.pressed(onevent_controller_1buttonUp_pressed_0)
controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
controller_1.buttonR1.released(onevent_controller_1buttonR1_released_0)
controller_1.buttonDown.pressed(onevent_controller_1buttonDown_pressed_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
