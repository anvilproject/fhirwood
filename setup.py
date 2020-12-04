import os
from setuptools import setup, find_packages

from fhirwood import __version__

root_dir = os.path.dirname(os.path.abspath(__file__))
req_file = os.path.join(root_dir, "requirements.txt")
with open(req_file) as f:
    requirements = f.read().splitlines()

setup(
    name="fhirwood",
    version = __version__,
    description=f"AnVIL fhirwood {__version__}",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    scripts=[],
)
