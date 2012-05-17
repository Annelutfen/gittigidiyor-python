# -*- coding: utf-8 -*-
#####################################################################
# Copyright (c) <2010> <GittiGidiyor>                               #
#                                                                   #
# Permission is hereby granted, free of charge, to any person       #
# obtaining a copy of this software and associated documentation    #
# files (the "Software"), to deal in the Software without           #
# restriction, including without limitation the rights to use,      #
# copy, modify, merge, publish, distribute, sublicense, and/or sell #
# copies of the Software, and to permit persons to whom the         #
# Software is furnished to do so, subject to the following          #
# conditions:                                                       #
#                                                                   #
# The above copyright notice and this permission notice shall be    #
# included in all copies or substantial portions of the Software.   #
#                                                                   #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,   #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES   #
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND          #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT       #
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,      #
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR     #
# OTHER DEALINGS IN THE SOFTWARE.                                   #
#####################################################################
from service import *
from jsonbuilder import *
from xmlbuilder import *

class CategoryService(Service):
    """
    This class represents the Category Service of the GittiGidiyor RESTLIKE API.
    """
    def __init__(self, auth):
        """
        Base Constructor. \n
        auth = Auth(username = 'testuser', password = 'testpassword', key = 'apikey', secret = 'apisecret') \n
        categoryApi = CategoryService(auth)
        """
        Service.__init__(self, "category", auth)
        self.headers = None

    def getCategories(self, startOffSet, rowCount, withSpecs, outputCT, lang):
        """
        Performs the 'getCategories' API method for the Category Service API of Gittigidiyor.\n
        startOffSet: is the offset in which category we are counting from.\n
        rowCount: is the number of how many categories will be fetched.\n
        withSpecs: if True, specifications are also fethced..\n
        outputCT: output content type (xml or json)\n
        lang: 'tr' or 'en'\n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/category?method=getCategories&outputCT=%s&startOffSet=%d&rowCount=%d&withSpecs=%s&lang=%s"
        if withSpecs:
            withSpecs = "true"
        else:
            withSpecs = "false"
        url = url % (outputCT, startOffSet, rowCount, withSpecs, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def getModifiedCategories(self, startOffSet, rowCount, changeTime, outputCT, lang):
        """
        Performs the 'getModifiedCategories' API method for the Category Service API of Gittigidiyor.\n
        startOffSet: is the offset in which category we are counting from.\n
        changeTime: datetime object\n
        rowCount: is the number of how many categories will be counted.\n
        withSpecs: if True, specifications are also fethced..\n
        outputCT: output content type (xml or json)\n
        lang: 'tr' or 'en'\n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/category?method=getModifiedCategories&outputCT=%s&startOffSet=%d&rowCount=%d&changeTime=%s&lang=%s"
        if lang == "tr":
            ct = datetime.datetime.strftime(changeTime, "%d/%m/%Y+%H:%M:%S")
        else:
            ct = datetime.datetime.strftime(changeTime, "%Y-%m-%d+%H:%M:%S")
        url = url % (outputCT, startOffSet, rowCount, ct, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def getCategory(self, categoryCode, withSpecs, outputCT, lang):
        """
        Performs the 'getCategory' API method for the Category Service API of Gittigidiyor.\n
        categoryCode: category code.\n
        withSpecs: if True, specifications are also fethced..\n
        outputCT: output content type (xml or json)\n
        lang: 'tr' or 'en'\n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/category?method=getCategory&outputCT=%s&categoryCode=%s&withSpecs=%s&lang=%s"
        if withSpecs:
            withSpecs = "true"
        else:
            withSpecs = "false"
        url = url % (outputCT, categoryCode, withSpecs, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def getCategorySpecs(self, categoryCode, outputCT, lang):
        """
        Performs the 'getCategorySpecs' API method for the Category Service API of Gittigidiyor.\n
        categoryCode: category code.\n
        outputCT: output content type (xml or json)\n
        lang: 'tr' or 'en'\n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/category?method=getCategorySpecs&outputCT=%s&categoryCode=%s&lang=%s"
        url = url % (outputCT, categoryCode, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content
