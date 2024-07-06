from distutils.core import setup

setup(
    name='Booking',
    version='0.1',
    author='Sourav',
    authoremail='souravdba@gmail.com',
    packages=['rentalhouse', 'travel'],
    scripts=['bin/install.sh'],
    url='https://pypi.python.org/pypi/Booking/',
    license='License.txt',
    description='Booking project',
    long_description=open('README.rst').read(),
    install_requires=[
     'pytz == 2017.2'
    ]
)