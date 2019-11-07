import os


def create_tsconfig(file_name):
    with open('tsconfig.json', 'w') as file:
        file.write('{\n')
        file.write('\t"compilerOptions": {\n')
        file.write('\t\t"module": "CommonJS",\n')
#        file.write('\t\t"noImplicitAny": true,\n')
        file.write('\t\t"removeComments": true,\n')
        file.write('\t\t"preserveConstEnums": true,\n')
        file.write('\t\t"outDir": "dist/",\n')
        file.write('\t\t"sourceMap": true,\n')
        file.write('\t\t"target": "esnext"\n')
        file.write('\t},\n')
        file.write('\t"include": [\n')
        file.write('\t\t"./{}.ts"\n'.format(file_name))
        file.write('\t]\n')
        file.write('}\n')

def delete_tsconfig():
    os.remove('./tsconfig.json')

def ts_config_file(file_name):
    if(not os.path.isfile('tsconfig.json')):
        #print('ts config file is not found, time to create a new one')
        create_tsconfig(file_name)
    else:
        #print('delete existing tsconfig and create our own')
        delete_tsconfig()
        create_tsconfig(file_name)
