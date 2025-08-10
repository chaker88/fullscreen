from setuptools import setup, find_packages

setup(
    name="fullscreen",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ipython",
    ],
    description="A small tool to display Vimeo fullscreen links in Jupyter notebooks.",
    author="Chaker Saidi",
    url="https://github.com/chaker88/fullscreen",
)
