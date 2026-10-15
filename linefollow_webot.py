from controller import Robot

def run_robot(robot):
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28

    # Motors
    left_motor = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")

    left_motor.setPosition(float("inf"))
    right_motor.setPosition(float("inf"))

    # IR sensors
    left_ir = robot.getDevice("ir0")
    right_ir = robot.getDevice("ir1")

    left_ir.enable(timestep)
    right_ir.enable(timestep)

    while robot.step(timestep) != -1:
        left_value = left_ir.getValue()
        right_value = right_ir.getValue()

        print("Left:", left_value, "Right:", right_value)

        left_speed = max_speed * 0.25
        right_speed = max_speed * 0.25

        # Original line-detection assumptions
        if left_value > right_value and 6 < left_value < 15:
            left_speed = -max_speed * 0.25

        elif right_value > left_value and 6 < right_value < 15:
            right_speed = -max_speed * 0.25

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
