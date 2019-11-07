import os
from subprocess import check_output
from shutil import rmtree
import shlex

def compile_ts_file():
    #we can assume all the steps 
    #delete dist dir
    if(os.path.isdir('./dist')):
        # print('Deleting the dist dir')
        rmtree('./dist')
    
    args = shlex.split('tsc')
    compile_output = check_output(args)
