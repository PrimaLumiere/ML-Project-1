from setuptools import find_packages,setup                  #it will automatically search for the packages in the project directory
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace('\n','') for req in requirements]                    #repalcing the '\n' at the end of package names
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(                  #meta data about the entire project                
name="ml_project_1",
version='0.0.1',
author="Ansuman",
author_email="am.prof.acc@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')                   #get_requirements will locate the path and install the required packages
)