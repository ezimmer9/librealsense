import os
import time
import sys
import subprocess as sp
import threading
import matplotlib.pyplot as plt
import numpy as np
from description import *


def event_switcher(line):
    switcher = {
        1: WAIT_TIMER,
        2: DEPTH_TIMER,
        3: RGB_TIMER
    }
    return switcher.get(int(line[0]) , lambda: "Invalid timer")


def parse_line(line):
    func = event_switcher(line)
    func.add_time(int(line[1]))
    func.add_typ(int(line[2]))
    #func.print_time_array()
    #func.print_typ_array()
    #print line
    
def collection_statistic():
    for i in range(NUM_OF_TIMERS):
        line = ["{0:d}".format(i+1) , i]
        func = event_switcher(line)
        a = []
        for j in range(func.size()):
            if (func.typs[j] == 0):
                start_time = func.times[j]
                #print start_time
            elif (func.typs[j] == 1):
                a.append((func.times[j] - start_time))
                #print "duration " + str((func.times[j] - start_time)) + " microsec"
        func.avg = np.average(a)
        func.std = np.std(a)
        func.median = np.median(a)
        print "Event name: " + func.name + " -  Median: " + str(func.median) +  ",   Average: " + str(func.avg) + ",   Std: " + str(func.std)


            
def usage():
    print("python script parse_timers:")
    print("parse_timers.py -f <PATH_TO_FILE>")

def main():
    argv = sys.argv
    print(argv)

    if sys.argv[1] == "-h":
        print("hello")
        usage()
        sys.exit()

    if len(sys.argv) < 3:
        print("to few parameters")
        usage()
        sys.exit()
    
    elif sys.argv[1] == "-f":
        PATH = argv[1+1]
    else:
        print("Only accepted arguments are -f and -h")
        sys.exit()
    counter = 0
    timers_file = open(PATH , 'r')
    timers_lines = timers_file.readlines()
    for i in range(len(timers_lines)):
        timers_lines_ns = timers_lines[i].replace("," , " ")
        mv_lines_s = timers_lines_ns.split()
        parse_line(mv_lines_s)
    timers_file.close()

    collection_statistic()

if __name__ == "__main__":
    main()
