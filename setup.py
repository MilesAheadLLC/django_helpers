from setuptools import setup, find_packages

setup(
    name = "django_helpers",
    version = "0.1",
    description = "Helper for Django Apps",
    packages = find_packages('.'),
    package_dir = {"":"."},
    package_data ={},
    install_requires = []
)