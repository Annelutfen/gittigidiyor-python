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

class CityService(Service):
    """
    This class represents the City Service of the GittiGidiyor RESTLIKE API.
    """
    def __init__(self, auth):
        """
        Base Constructor. \n
        auth = Auth(username = 'testuser', password = 'testpassword', key = 'apikey', secret = 'apisecret') \n
        cityApi = CityService(auth)
        """
        Service.__init__(self, "city", auth)
        self.headers = None

    def getCities(self, startOffSet, rowCount, outputCT, lang):
        """
        Performs the 'getCities' API method for the City Service API of Gittigidiyor.\n
        startOffSet: is the offset in which city we start counting from.\n
        rowCount: is the number of how many cities will be fetched.\n
        outputCT: output content type (xml or json)\n
        lang: 'tr' or 'en'\n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/city?method=getCities&outputCT=%s&startOffSet=%d&rowCount=%d&lang=%s"
        url = url % (outputCT, startOffSet, rowCount, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def getModifiedCities(self, startOffSet, rowCount, changeTime, outputCT, lang):
        """
        Performs the 'getModifiedCities' API method for the City Service API of Gittigidiyor.\n
        startOffSet: is the offset in which city we start counting from.\n
        rowCount: is the number of how many cities will be fetched.\n
        changeTime: is a datetime object.\n
        outputCT: output content type (xml or json)\n
        lang: 'tr' or 'en'\n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/city?method=getModifiedCities&outputCT=%s&changeTime=%s&startOffSet=%d&rowCount=%d&lang=%s"
        if lang == "tr":
            ct = datetime.datetime.strftime(changeTime, "%d/%m/%Y+%H:%M:%S")
        else:
            ct = datetime.datetime.strftime(changeTime, "%Y-%m-%d+%H:%M:%S")
        url = url % (outputCT, ct, startOffSet, rowCount, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content
    
    def getCity(self, code, outputCT, lang):
        """
        Performs the 'getCity' API method for the City Service API of Gittigidiyor.\n
        code: code id of the city.\n
        outputCT: output content type (xml or json)\n
        lang: 'tr' or 'en'\n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/city?method=getCity&outputCT=%s&code=%s&lang=%s"
        url = url % (outputCT, code, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content
