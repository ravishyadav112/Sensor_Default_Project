from setuptools import setup , find_packages
from typing import List

HYPEN_E_DOT = '-e.'
def get_requirements(path : str) -> List[str]:
    requirements=[]
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="Sensor_Default_Prediction",
    version= "0.0.1",
    description="To build a project on Sensor_Default_prediction",
    author="Ravish",
    author_email="ravishkumar1242@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")

)