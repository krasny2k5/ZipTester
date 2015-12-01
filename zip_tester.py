#!/usr/bin/python    

#                    Joaquin Escayo @ 2015                    #
# Test all zip files within a directory specified as argument #

import sys
import getopt
import os
import ConfigParser as configparser
from StringIO import StringIO
import zipfile

def usage():
    print '''usage: %s [-D path|-o path|-v]''' % sys.argv[0]

def help():
    print '''
usage: %s [-D path|-o path|-v]
    -D <path> directory where the zipfiles are, by default current directory is used
    -o  overwrite data .zip file even if it exists
    -v  run verbosely
''' % sys.argv[0]

output = False
verbose = False
directory = os.getcwd()

try:
    opts, args = getopt.getopt(sys.argv[1:],'vD:o:')
except getopt.GetoptError:
    usage()
    sys.exit(3)

for opt, arg in opts:
    if opt == '-D':
        directory = arg
    if opt == '-o':
        output = True
        log = arg
    if opt == '-v':
        verbose = True
    if opt == '-h':
        help()
        sys.exit(5)

if output:
    if os.path.isfile(log):
        print "%s file exists!" % log
        sys.exit(5)
    else:
        outfile = open(log,'w')

for file in os.listdir(directory):
    if zipfile.is_zipfile(file):
        z = zipfile.ZipFile(file,'r')
        if z.testzip() is not None:
            print "%s file is CORRUPTED" % file
            if output:
                outfile.write('%s \n' % file)
        else:
            if verbose:
                print "%s file is OK" % file
        z.close()
    else:
        if verbose:        
            print "%s is not a zipfile" % file

if output:
    outfile.close()


