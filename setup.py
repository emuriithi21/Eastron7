from distutils.core import setup

setup(
    name='Eastron',
    version='1.1',
    url='none',
    license='none',
    author='cmuriithi',
    author_email='emuriithi21@outlook.com',
    description='Eastron Smart Meter agent',
    py_modules=['certifi', 'chardet' , 'idna', 'pyserial' , 'requests', 'urllib3'],
    entry_points={

                   'console_scripts': [

                       'Eastron_agent = Eastron_agent:main'

                   ]

               },
)
