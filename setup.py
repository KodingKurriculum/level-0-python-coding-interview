from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


requirements = parse_requirements('requirements.txt')

setup(
    name='practice-problems',
    version='0.1.1',
    description='A set of common practice problems and algorithms',
    author='Karl Haviland',
    author_email='youcancode@kodingkurriculum.com',
    url='http://github.com/kodingkurriculum/practice-problems',
    packages=['practice_problems'],
    install_requires=requirements
)