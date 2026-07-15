from setuptools import setup, find_packages

setup(
    name="urbanchangeai",
    version="0.1.0",
    packages=find_packages(include=["urbanchangeai", "urbanchangeai.*"]),
    install_requires=[
        line.strip() for line in open("requirements.txt").readlines() if line.strip() and not line.startswith("#")
    ],
    include_package_data=True,
    python_requires=">=3.9",
)
