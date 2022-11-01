from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="ntrprtr_bitlocker_forensics",
    version="0.1.0",
    author="5f0",
    url="https://github.com/5f0ne/ntrprtr-bitlocker-forensics",
    description="ntrprtr configurations for forensic analysis of bitlocker volumes",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    include_package_data=True,
    package_data={
        "ntrprtr_bitlocker_forensics.config": ["bitlocker-volume-header.json",
                                               "bitlocker-metadata-header.json"]
    },
    install_requires=[
    
    ],
     entry_points={
        "console_scripts": [
            "ntrprtr_bitlocker_forensics = ntrprtr_bitlocker_forensics.__main__:main"
        ]
    }
)
