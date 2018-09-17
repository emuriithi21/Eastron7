from distutils.core import setup

setup(
    name='Eastron',
    version='1.1',
    url='none',
    license='none',
    author='cmuriithi',
    author_email='emuriithi21@outlook.com',
    description='Eastron Smart Meter agent',
    py_modules=['Eastron_agent', 'com_ports','cumulocity_REST'],
    entry_points={

                   'console_scripts': [

                       'eastronagent = Eastron_agent:main'

                   ]

               },
)
