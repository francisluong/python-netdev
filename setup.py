from setuptools import setup

#parse requirements
req_lines = [line.strip() for line in open("requirements.txt").readlines()]
install_reqs = list(filter(None, req_lines))

setup(
    name = "auth-userpass",
    version = "0.0.1",
    author = "Francis Luong (Franco)",
    author_email = "networkascode@definefunk.com"
    description = "Simple but not so secure username and password handling",
    license = "MIT"
    url = "https://github.com/francisluong/PyJNX"
    install_requires=install_reqs
)
