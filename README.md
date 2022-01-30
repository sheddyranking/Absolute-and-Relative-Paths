# Absolute-and-Relative-Paths

ABSOLUTE IMPORTS/PATH
#use this approach when you are triversing within and outside the folder

Examples in package1 file 1
from package1 import file2 
from package1.sub_package import file
from package2 import file1

RELATIVE IMPORT/PATH

#this are used only when you are triversing within the folder.
#it returns an error once it hits the root folder thats why its better to use the absolute path.

Example in package1 file 3
from . import file1
from . import file2
from .sub_package import file

#import within the same parent folder
example in sub_package1 file
from .. import file2

Run all the files in root_file.py
