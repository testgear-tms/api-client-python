from setuptools import setup

setup(
    name='testgear-api-client',
    version='1.0.0',
    description='API-client for TestGear',
    long_description=open('README.md', "r").read(),
    long_description_content_type="text/markdown",
    url='https://pypi.org/project/testgear-api-client/',
    author='Pavel Butuzov',
    license='Apache-2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    py_modules=['testgear_api_client'],
    packages=['testgear_api_client'],
    package_dir={'testgear_api_client': 'src'},
    install_requires=['requests']
)
