import setuptools

def readme():
    with open("README.md", "r",encoding="utf8") as fh:
        long_description = fh.read()
    return long_description

setuptools.setup(
    name="split_ratio",
    version="1.0.1",
    author="Saicharan Papani",
    author_email="charansai850@gmail.com",
    description="Split ratio, information gain utilities",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/papanisaicharan/split-ratio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)