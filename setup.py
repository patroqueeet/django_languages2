from distutils.core import setup

setup(
    name="Languages2",
    version="0.0.6",
    author="Patroqueeet",
    author_email="jirka@tschitschereengreen.com",
    packages=["languages2"],
    description="forked unmainted repo",
    long_description=open("README.txt").read(),
    install_requires=["Django >= 3.2",],
)
