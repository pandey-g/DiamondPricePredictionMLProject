from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filePath : str) ->List[str] : 
    requirements = []
    with open(filePath) as fileObj :
        requirements = fileObj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(

    name = 'DiamondPricePrediction',
    version = '0.0.1',
    author = 'Law Bind Pandey',
    author_email = 'lawbindpandey01@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()

)
