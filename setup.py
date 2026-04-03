from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This Function Will Return List OF Requiremnts
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #ReadLInes from the line
            lines=file.readlines()
            
            for line in lines:
                requirement=line.strip()
                ## ignore -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
                    
    except FileNotFoundError:
        print("Requiremnt file not Found")
    
    return requirement_lst


setup(
    name="NetWork Security",
    version="0.0.0.1",
    author="Om Kulkarni",
    author_email="justmeaprogrammer@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
    
)