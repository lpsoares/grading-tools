import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# From: igordsm@gmail.com

setuptools.setup(
    name="grading-tools", # Replace with your own username
    version="0.0.1a",
    author="Igor Montagner / Luciano Soares",
    author_email="lpsoaresm@gmail.com",
    description="Tools for creating autograders.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lpsoares/grading_tools",
    install_requires=['psutil'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
