import os

def raw(args):
    # receive string arguments from command line
    # return a string of target path
    assert len(args) >= 1, 'pcd function "raw" expects at least one argument'
    return os.path.join(*args)