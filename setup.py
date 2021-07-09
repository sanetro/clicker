from setuptools import setup
from setuptools import find_packages

setup(
	name="Ciggarette-Clicker",
	version="1.0.0",
	description="I have made this for fun and to lern something.",
	author="Sanetro",
	author_email="sanetro26@gmail.com",
	packages=find_packages(),
	url="no:url",license="GNU opensource",	
	include_package_data=False,
	entry_points={
		'console_scripts': [
			'Ciggarette-Clicker = Ciggarette-Clicker.main:main'
		]
	}	
)