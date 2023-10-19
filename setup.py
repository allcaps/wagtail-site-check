import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wagtail-site-check",
    version="0.0.1",
    author="Coen van der Kamp",
    author_email="coen@fourdigits.nl",
    description="A Wagtail app to check the configuration of Wagtail Sites.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allcaps/wagtail-site-check",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 4",
        "Framework :: Wagtail :: 5",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
    python_requires=">=3.7",
    include_package_data=True,
)
