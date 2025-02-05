from setuptools import  setup

setup(
    name='cosi',
    version='0.0.8',
    description='FIC coin simulator',
    url='https://github.com/TIC-Quant/coin_simulator.git',
    author='DoyoonKim',
    author_email='vitainu0104@unist.ac.kr',
    packages=['cosi'],
    zip_safe=False,
    install_requires=[
        'pyupbit==0.2.33',
        'pandas==2.0.1',
        'matplotlib'
        ]
)
