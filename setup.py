from setuptools import setup

setup(
    name='monkey',
    version='1.0',
    py_modules=['monkey'],
    include_package_data=True,
    install_requires=[
        'click'
        # Colorama is only required for Windows.
    ],
    entry_points='''
        [console_scripts]
        monkey=monkey.monkey:cli
    ''',
    license='MIT',
    author='Yicheng Zhang',
    url='https://github.com/lancevalour/monkey'
)