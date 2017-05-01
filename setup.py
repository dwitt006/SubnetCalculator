# Title:     Subnet Calculator: Setup
# Date:      04-19-2017


from setuptools import setup


setup(
    name='SubnetCalculator',
    version='1.0',
    license='MIT',
    description='Calculate subnet variables',
    long_description=open('README').read(),
    packages=['SubnetCalculator'],
    test_suite='tests',
    author='Draper Wittkopp',
    entry_points={
        'gui_scripts': ['SubnetCalc=SubnetCalculator.SubnetCalculatorGUI:SubnetCalculatorGUI'],
        'console_scripts': ['SubnetCalc=SubnetCalculator.SubnetCalculatorGUI:SubnetCalculatorGUI']}
    # install_requires=[]
)
