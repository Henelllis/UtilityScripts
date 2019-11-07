import os
import sys
import argparse
import glob
from ts_config_logic import ts_config_file
from compile_ts_logic import compile_ts_file
from run_js_logic import run_node

def validate_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='file to compile and run')
    args = parser.parse_args()
    return args.file

def valid_file(argFile):
    if(not os.path.isfile('./{}'.format(argFile))):
        print('Unable to find file {}'.format(argFile))
        return False

    filename, file_extension = os.path.splitext(argFile)
    if(file_extension != ".ts"):
        print('Incorrect file format, unable to compile you DINGUS')
        return False
    
    return True

def compile():
    try:
        compile_ts_file()
    except Exception as exception:
        print('Error in Compiling :: {}'.format(exception))
        sys.exit(1)            

def locate_and_run_file(argFile):

    if(not valid_file(argFile)):
        return

    # print('You found it Henry FINALLY GAAAAAAAAAAAAAAAAAAAAAAAH!!!!!');
    file_base_name = argFile[:-3]
    ts_config_file(file_base_name)
    compile()
    run_node(file_base_name)
    


def run_script():
    argsFile = validate_args()
    locate_and_run_file(argsFile)


if __name__ == '__main__':
    run_script()
