from setuptools import setup, find_packages  # noqa: H301

NAME = "testgear-api-client"
VERSION = "3.1.0"
REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="API-client for Test Gear",
    long_description=open('README.md', "r").read(),
    long_description_content_type="text/markdown",
    author="Integration team",
    author_email="integrations@test-gear.io",
    url="https://pypi.org/project/testgear-api-client/",
    py_modules=['testgear_api_client'],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=REQUIRES,
    include_package_data=True
)
