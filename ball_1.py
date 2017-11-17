# ball_1.py
""" Initial program to calulate the helight of a ball
    thrown with an initial velocity"""

def main():
    """ Main program"""

    velocity_initial = 5    # initial velocity of ball
    accel_grav = 9.81       # acceleration due to gravity
    time = 0.6              # elapsed time

    height = (velocity_initial * time) - (0.5 * accel_grav * (time ** 2))

    print("At time =", time, "s, the height of the ball is", height, "m.")


main()
