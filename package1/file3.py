#Relative import

from . import file1
from . import file2
from .sub_package import file

def run_file3():
    file1.relative_file1()
    file2.relative_file2()
    file.sub_relative_file()

