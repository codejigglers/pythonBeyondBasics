#Packages are represented as a directory in the file system while module is represented as a file in the file system.

#Python looks in the sys.path for finding the requested module in the import statement.

#If we create a module not mentioned in the sys.path we can simply append to it.


import test_module

#It will not import but if we add not_searched in the sys.path, it will look for it

import sys

sys.path.append("not_searched")
import not_searched

#See its searching now


#If we want to import a module from a directory use from directory import module
#Then you can use the module's methods

from not_searched import test_module

