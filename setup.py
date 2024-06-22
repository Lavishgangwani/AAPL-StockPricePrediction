#setup.py

from setuptools import find_packages,setup
from typing import List




HYPEN_E_DOT = '-e .'
#Create a Function to link requirements.txt with setup.py
def get_requirements(file_path:str)->List[str]:
    """
    This function will handle all the install requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements





setup(
    name='StockPricePrediction',
    version='0.0.1',
    author='Lavish Gangwani',
    author_email='lavishgangwani22@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)