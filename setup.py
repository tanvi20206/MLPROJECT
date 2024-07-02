## basic information are listed in this

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''this function will return the requirement'''
    requirements=[]

    with open(file_path)as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]

    return requirements

setup(
    name= 'mlproject',
    version='0.0.1',
    author ='Tanvi',
    author_email='tanvigupta848@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)


## to run this type python setup.py install