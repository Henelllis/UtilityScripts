import os
import argparse
import glob
from ts_config_logic import ts_config_file

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
    print('filename: {}'.format(filename))
    print('file extension {}'.format(file_extension))
    if(file_extension != ".ts"):
        print('Incorrect file format, unable to compile you DINGUS')
        return False
    
    return True


def locate_and_run_file(argFile):

    if(not valid_file(argFile)):
        return

    print('You found it Henry FINALLY GAAAAAAAAAAAAAAAAAAAAAAAH!!!!!');
    ts_config_file(argFile[:-3])
    


def run_script():
    print('test')

    argsFile = validate_args()

    locate_and_run_file(argsFile)
    #Compile the code
        #Check to see if there exists in ts config
        #if so delete it and provide it from this code
        #Seperate file to handle generating the tsconfig
        #Replace the compile object names and outputs
    
    #Invoke a subprocess call and wait till compilition is finished
    #After you get the result if it failed our not, need to figure out if failed or not
    #check output final line, will be fun to figure out

if __name__ == '__main__':
    run_script()




