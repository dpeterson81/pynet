
from my_func import print_hello
import os

#call print_hello from current directory
print "Calling function with module installed in current directory"
print_hello()

#Move file to random subdir
os.rename("./my_func.py", "./random/subdir/my_func.py")
print "Calling function with module in ./random/subdir/"
print_hello()

#Move file to ~/applied_python/lib/python2.7/site-packages/
os.rename("./random/subdir/my_func.py", "/home/dpeterson/applied_python/lib/python2.7/site-packages/my_func.py")
print "Calling function with module in ~/applied_python/lib/python2.7/site-packages/"
print_hello()

os.rename( "/home/dpeterson/applied_python/lib/python2.7/site-packages/my_func.py", "./my_func.py")
