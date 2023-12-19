from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This will return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]


        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements


setup(
name='first_mlproject',
version='0.0.1',
author='Osama Bin Naeem',
author_email='chosama7777@gmail.com',
packages=find_packages(),
install_requirements=get_requirements('requirement.txt'),




)