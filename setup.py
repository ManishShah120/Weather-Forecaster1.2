import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="Weather-Forecaster1.2-ManishShah120",
	version="1.2",
	author="Manish Kumar Shah",
	author_email="mkshah141@gmail.com",
	description="Weather Report of any State in India",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/ManishShah120/Weather-Forecaster1.2",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
