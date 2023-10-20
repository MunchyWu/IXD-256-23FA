<<<<<<< HEAD
# blink an LED connected to pin G1 on and off
=======
# blink an LED connected to pin 1 on and off
>>>>>>> 018dc8dd1fd0afd638406bbb264469aa44f52f98

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

<<<<<<< HEAD
=======
# global pin1 variable:
>>>>>>> 018dc8dd1fd0afd638406bbb264469aa44f52f98
pin1 = None

def setup():
  global pin1
<<<<<<< HEAD

  M5.begin()
=======
  # initialize M5 board:
  M5.begin()
  # initialize pin1 as an output pin:
>>>>>>> 018dc8dd1fd0afd638406bbb264469aa44f52f98
  pin1 = Pin(1, mode=Pin.OUT)

def loop():
  global pin1
<<<<<<< HEAD
  M5.update()
  pin1.on()
  time.sleep(1)
=======
  # update M5 board:
  M5.update()
  # turn pin1 on (high) and sleep for 1 second:
  pin1.on()
  time.sleep(1)
  # turn pin1 off (low) and sleep for 1 second:
>>>>>>> 018dc8dd1fd0afd638406bbb264469aa44f52f98
  pin1.off()
  time.sleep(1)

if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
