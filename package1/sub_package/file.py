#relative import
from .. import file2

def sub_package1_file():
    print("sub_package1_file")
    
def test():
    file2.package1_file2()

def sub_relative_file():
    print("sub_relative_file")

    