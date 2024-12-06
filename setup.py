from setuptools import setup, find_packages

setup(
    name='simple_math_package',            # Package name
    version='0.1.0',                       # Version number
    packages=find_packages(),             # Automatically find all packages
    install_requires=[],                   # No external dependencies for this simple example
    author='Aung Myo Tun',
    author_email='aungmyotun1115@gmail.com',
    description='A simple package for basic math operations.',
    long_description=open('README.md').read(),  # Description from README file
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/simple_math_package',  # URL of your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
