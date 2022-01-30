from package1 import file2 #absolute import
from package1.sub_package import file
from package2 import file1



def run():
    file2.package1_file2()
    file.sub_package1_file()
    file1.package2_file1()




