# -*- coding: utf-8 -*-
from distutils.core import setup

setup(name = "python-gittigidiyor",
      version = "1.0",
      description = "GittiGidiyor RESTLIKE API",
      author = "Ozgur Vatansever",
      license = open("LICENSE").read(),
      long_description = open("README").read(),
      author_email = "ozgurvt@gmail.com",
      url = "http://dev.gittigidiyor.com",
      packages = ["gittigidiyor"],
      install_requires=['setuptools', 'httplib2', 'simplejson'],
      platforms = ["linux"])
