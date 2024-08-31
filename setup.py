# setup.py
from setuptools import setup, find_packages

setup(
    name='ai_receptionist',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'qdrant-client',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'run-server=app.main:app',
        ],
    },
)
