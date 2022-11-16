import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1' 
PACKAGE_NAME = 'funciones' 
AUTHOR = 'Juan Pedro Hurtado'
AUTHOR_EMAIL = 'juan.hurtado@co.idom.com'
URL = 'https://github.com/Juanpepitt/crtmfuncs.git'

LICENSE = 'MIT'
DESCRIPTION = 'obtiene funciones contenidas en un .py ubicado en un bucket de AWS S3' 
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'sys',
      'boto3',
      'json',
      'importlib',
      'abc'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)