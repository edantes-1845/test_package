import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="test-package-username",
    version="0.2",
    author="Your Name",
    author_email="your_email",
    description="This is a test package.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="package_github_page",
    packages=['test_package'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)