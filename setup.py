
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='SelfDZSR',
    version='0.0.1',
    author='Tsz Fung Yau',
    author_email='yaurf44@gmail.com',
    description='SelfDZSR Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/XDMickeyYau/SelfDZSR',
    project_urls = {
        "Bug Tracker": "https://github.com/XDMickeyYau/SelfDZSR/issues"
    },
    packages=['SelfDZSR'],
    install_requires=[],
)