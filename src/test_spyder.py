#!/usr/bin/env python

# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import sys

# Import the PCA9685 module.
import Adafruit_PCA9685
import rospy

from classes.spyder_handler import *

class test_spyder:
    def __init__(self):
        # Initialise the PCA9685 using the default address (0x40).
        self.adafruit_servo_i2c = Adafruit_PCA9685.PCA9685()
        self.adafruit_servo_i2c.set_pwm_freq(60)

        self.sp_handler = SpyderHandler(self.adafruit_servo_i2c)

        #self.reset_spyder()

        while not rospy.is_shutdown():
            self.sp_handler.move('2.1', 20)
            self.sp_handler.move('2.2', 0)
            self.sp_handler.move('2.3', 50)

            self.sp_handler.move('3.1', 80)
            self.sp_handler.move('3.2', 100)
            self.sp_handler.move('3.3', 50)

            self.sp_handler.move('5.1', 30)
            self.sp_handler.move('5.2', 30)

            time.sleep(1)

            self.sp_handler.move('2.1', 80)
            self.sp_handler.move('2.2', 100)
            self.sp_handler.move('2.3', 50)

            self.sp_handler.move('3.1', 20)
            self.sp_handler.move('3.2', 0)
            self.sp_handler.move('3.3', 50)

            self.sp_handler.move('5.1', 70)
            self.sp_handler.move('5.2', 70)

            time.sleep(1)


    def on_shutdown(self):
        self.reset_spyder()

    def reset_spyder(self):
        # restart spyder
        self.sp_handler.move('1.1', 50)
        self.sp_handler.move('1.2', 50)
        self.sp_handler.move('1.2', 50)
        self.sp_handler.move('2.1', 50)
        self.sp_handler.move('2.2', 50)
        self.sp_handler.move('2.3', 50)
        self.sp_handler.move('3.1', 50)
        self.sp_handler.move('3.2', 50)
        self.sp_handler.move('3.3', 50)
        self.sp_handler.move('4.1', 50)
        self.sp_handler.move('4.2', 50)
        self.sp_handler.move('4.3', 50)
        self.sp_handler.move('5.1', 50)
        self.sp_handler.move('5.2', 50)


def main(args):
    rospy.init_node('spyder_node', anonymous=True)

    ic = test_spyder()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")


if __name__ == '__main__':
    main(sys.argv)