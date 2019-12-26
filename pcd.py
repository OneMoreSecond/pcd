import os
import sys
import argparse
import importlib.util

failures = {
    'invalid_function_name': 'function name starting with an underscore is not supported',
    'function_not_found': 'function name is not found in the function script',
}

def fail(message):
    raise Exception('pcd error: ' + failures[message])


pcd_dir = os.path.dirname(os.path.abspath(__file__))
default_function_script_path = os.path.join(pcd_dir, 'function.py')

parser = argparse.ArgumentParser(prog='pcd', description='print a path returned by a function call to the function script')
parser.add_argument('-s', '--script', dest='function_script_path', metavar='PATH', default=default_function_script_path, help='specify the path of function script')
parser.add_argument('-c', '--command', dest='command_pattern', metavar='PATTERN', help='execute the command pattern after a path is printed')
parser.add_argument('-i', '--interactive', dest='interactive', action='store_true', help='enter interactive mode')
parser.add_argument('-k', '--keep-module', dest='keep_module', action='store_true', help='only load function script module once')
parser.add_argument('call', nargs='*', help='the function call to get path')

args = parser.parse_args()

spec = importlib.util.spec_from_file_location("functions", args.function_script_path)
functions = None
def get_function(name):
    global functions
    if not args.keep_module or functions is None:
        functions = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(functions)
    return getattr(functions, name)

def get_path(call):
    if len(call) == 0:
        return
    
    try:
        function_name = call[0]
        if function_name[0] == '_':
            fail('invalid_function_name')

        function = get_function(function_name)
        if function is None:
            fail('function_not_found')

        path = function(call[1:])
        print(path)

        if args.command_pattern is not None:
            os.system(args.command_pattern.format(path))
    except Exception as e:
        print(e)

get_path(args.call)

if args.interactive:
    try:
        while True:
            line = input('pcd> ')
            call = line.strip().split()
            get_path(call)
    except KeyboardInterrupt:
        pass