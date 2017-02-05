#!/usr/bin/env python

"""
    led_flusher.py
    Copyright (C) 2017  Kenta Iguchi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import rospy
from std_msgs.msg import Bool

def led1_callback(msg):
	with open("/dev/myled0", "w") as f:
		f.write("1\n" if msg.data else "0\n")

def led2_callback(msg):
	with open("/dev/myled0", "w") as f:
		f.write("3\n" if msg.data else "2\n")

def led3_callback(msg):
	with open("/dev/myled0", "w") as f:
		f.write("5\n" if msg.data else "4\n")

def led4_callback(msg):
	with open("/dev/myled0", "w") as f:
		f.write("7\n" if msg.data else "6\n")

if __name__ == "__main__":
	rospy.init_node("led_flusher")
	sub1 = rospy.Subscriber("led1", Bool, led1_callback, queue_size=10)
	sub2 = rospy.Subscriber("led2", Bool, led2_callback, queue_size=10)
	sub3 = rospy.Subscriber("led3", Bool, led3_callback, queue_size=10)
	sub4 = rospy.Subscriber("led4", Bool, led4_callback, queue_size=10)
	rospy.spin()
