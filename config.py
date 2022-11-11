import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class Config(object):
    BRAND = os.environ.get('logo.png') 

