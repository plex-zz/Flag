#!/bin/env python2.5

import os, sys
import string

def search_pkg(pkg, pkgsrc_path):
    """Search a given package in the pkgsrc path
    """
    for dir in os.listdir(pkgsrc_path):
        ignored = ['.git', 'CVS', 'Makefile', 'README', 'bootstrap',
            'doc', 'mk', 'pkglocate' ]
        if dir not in ignored:
            for subdir in os.listdir(pkgsrc_path + dir):
                if subdir == pkg:
                    return pkgsrc_path + dir + '/' + subdir
                    
def install_pkg(pkg, pkgsrc_path):
    pkg = search_pkg(pkg, pkgsrc_path)
    os.chdir(pkg)
    os.system("bmake install clean")
    
def bootstrap(pkgsrc_path):
    os.chdir(pkgsrc_path + 'bootstrap')
    os.system("rm -r work")
    os.system("./bootstrap")
    
if __name__ == '__main__':
    pkgsrc_path = '/usr/pkgsrc/'
    if sys.argv[1] == 'bootstrap':
        bootstrap(pkgsrc_path)
    else:
        install_pkg(sys.argv[1], pkgsrc_path)
