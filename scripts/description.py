import os
import time
import sys
import subprocess as sp
import threading
import matplotlib.pyplot as plt
import numpy as np


class event:

    def __init__(self, name):
        self.name = name
        self.times = []
        self.typs = []
        self.avg = []
        self.std = []
        self.median = []

    def add_time(self , time):
        self.times.append(time)
        
    def add_typ(self , typ):
        self.typs.append(typ)
        
    def print_time_array(self):
        print self.times

    def print_typ_array(self):
        print self.typs

    def size(self):
        return len(self.typs)

WAIT_TIMER = event("WAIT")
DEPTH_TIMER = event("DEPTH")
RGB_TIMER = event("RGB")

# timers descirtion
NUM_OF_TIMERS = 3
WAIT = 1
DEPTH = 2
RGB = 3
