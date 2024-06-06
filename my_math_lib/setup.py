from setuptools import setup, find_packages

setup(
    name="my_math_lib",
    version="0.1",
    packages=find_packages(),
    description="A simple math library for arithmetic and geometry calculations",
    author="Masaki",
    author_email="happy.engineer.life@gmail.com",
    url="https://github.com/masakiShito/sample-code/my_math_lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
