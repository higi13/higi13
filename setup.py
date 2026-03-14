from setuptools import setup, find_packages

setup(
    name="higi13-profile",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'fastapi>=0.104.1',
        'uvicorn>=0.24.0',
    ],
)
