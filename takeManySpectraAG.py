import numpy as np
import os
import time
import argparse

parser = argparse.ArgumentParser(description='Usage: python takeManySpectraAG.py --command <input some command string>')
parser.add_argument('--command', type=str, nargs=1, help='If defined, becomes the command line executed.  Make sure the Agilent is hooked up to the PLL control signal.')

args = parser.parse_args()

if args.command is not None:
  commands = args.command[0]
else:
  commands = np.array(['./AGmeasure SPAG4395Atemplate_5MHzStop.yml', 
                       './AGmeasure SPAG4395Atemplate_100kHzStop.yml', 
                       './AGmeasure SPAG4395Atemplate_10kHzStop.yml', 
                       './AGmeasure SPAG4395Atemplate_1kHzStop.yml'])

number = len(commands)
print 'Commands: ', commands
print 'Number:  ', number
print 
startTime = time.time()
for ii, command in enumerate(commands):
  print
  print 'Starting Measurement ', ii
  print command
  os.system(command)
  print
  print 'Measurement ', ii,' finished in ', time.time() - startTime, ' seconds'
  print
  print '---------------------------------------------------------------------'
