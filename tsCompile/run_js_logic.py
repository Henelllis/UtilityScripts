import os
import sys
from subprocess import Popen, PIPE
import shlex

def run_node(filename):
    #Assume no args for JS Process
    args = shlex.split('node ./dist/{}.js'.format(filename))
    stdout, stderr = Popen(args, stdout=PIPE, stderr=PIPE).communicate()
    print(stdout.decode('utf-8'))



#Get the cwd
#assume the `/dist is a valid path`
#change working dir to cwd + /dist
#then execute via Popen or Communicate 


