from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='glimmr',
    version='1.1.3',
    packages=['glimmr'],
    package_dir={'':'src'},
    url='https://github.com/d8ahaard/python-glimmr',
    license='MIT',
    author='d8ahazard',
    author_email='donate.to.digitalhigh@gmail.com',
    description='An asynchronous library to control Glimmr devices.',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
