#!/usr/bin/env python

"""
    led_pub.py
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

if __name__ == "__main__":
	rospy.init_node("led_pub")
	pub1 = rospy.Publisher("led1", Bool, queue_size=10)
	pub2 = rospy.Publisher("led2", Bool, queue_size=10)
	pub3 = rospy.Publisher("led3", Bool, queue_size=10)
	pub4 = rospy.Publisher("led4", Bool, queue_size=10)
	rate = rospy.Rate(10)

	pub1.publish(False)
	pub2.publish(False)
	pub3.publish(False)
	pub4.publish(False)

	try:
		while not rospy.is_shutdown():
			pub1.publish(True)
			pub2.publish(False)
			pub3.publish(False)
			pub4.publish(False)
			rate.sleep()
			pub1.publish(True)
			pub2.publish(True)
			pub3.publish(False)
			pub4.publish(False)
			rate.sleep()
			pub1.publish(True)
			pub2.publish(True)
			pub3.publish(True)
			pub4.publish(False)
			rate.sleep()
			pub1.publish(True)
			pub2.publish(True)
			pub3.publish(True)
			pub4.publish(True)
			rate.sleep()
			pub1.publish(False)
			pub2.publish(True)
			pub3.publish(True)
			pub4.publish(True)
			rate.sleep()
			pub1.publish(False)
			pub2.publish(False)
			pub3.publish(True)
			pub4.publish(True)
			rate.sleep()
			pub1.publish(False)
			pub2.publish(False)
			pub3.publish(False)
			pub4.publish(True)
			rate.sleep()
			pub1.publish(False)
			pub2.publish(False)
			pub3.publish(False)
			pub4.publish(False)
			rate.sleep()
	except rospy.KeybordInterrupt:
		pass
