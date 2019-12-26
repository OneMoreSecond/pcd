def raw(*args):
    # receive string arguments from command line
    # return a string to change to target directory
    assert len(args) == 1, 'pcd function "raw" expects exact one argument'
    return args[0]