from setuptools import setup
import subprocess

#parse requirements
req_lines = [line.strip() for line in open("requirements.txt").readlines()]
install_reqs = list(filter(None, req_lines))

setup(
    name = "netdev",
    version = "0.0.1",
    author = "Francis Luong (Franco)",
    author_email = "networkascode@definefunk.com",
    description = ("Network device interactions over SSH"),
    license = "LICENSE.txt",
    url = "https://github.com/francisluong/python-netdev",
    install_requires=install_reqs,
    packages=['netdev'],
    test_suite = "nose.collector"
)



