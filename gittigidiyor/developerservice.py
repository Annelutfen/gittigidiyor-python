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

class DeveloperService(Service):
    """
    This class represents the Developer Service of the GittiGidiyor RESTLIKE API.
    """
    def __init__(self, auth):
        """
        Base Constructor.
        """
        Service.__init__(self, "developer", auth)
        self.headers = None

    def isDeveloper(self, nick, password, inputCT, outputCT, lang):
        """
        Performs the 'isDeveloper' API method for the Developer Service API of Gittigidiyor.\n
        nick: Gittigidiyor.com nickname of the user. \n
        password: Gittigidiyor.com password of the user. \n
        inputCT: input content type (xml or json) \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en' \n
        """
        if not inputCT in ("xml", "json"):
            raise Exception("Gondereceginiz veriyi yalnizca xml ya da json tipinde gonderebilirsiniz.")
        
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/developer?method=isDeveloper&outputCT=%s&inputCT=%s&lang=%s"
        url = url % (outputCT, inputCT, lang)
        
        if inputCT == "xml":
            builder = XMLBuilder()
            elements = builder.createElementsWithTextNodes(nick = nick, password = password)
            builder.appendListOfElementsToElement(builder.root(), elements)
            body = builder.toxml()
        else:
            body = JSONBuilder.getJSONObj(nick = nick, password = password)
            
        response, content = self.makeRequest(url, method = "POST", body = body, inputCT = inputCT)
        self.headers = response
        return content

    def registerDeveloper(self, nick, password, inputCT, outputCT, lang):
        """
        Performs the 'registerDeveloper' API method for the Developer Service API of Gittigidiyor. \n
        nick: Gittigidiyor.com nickname of the user. \n
        password: Gittigidiyor.com password of the user. \n
        inputCT: input content type (xml or json) \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en' \n
        """
        if not inputCT in ("xml", "json"):
            raise Exception("Gondereceginiz veriyi yalnizca xml ya da json tipinde gonderebilirsiniz.")
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/developer?method=registerDeveloper&outputCT=%s&inputCT=%s&lang=%s"
        url = url % (outputCT, inputCT, lang)

        if inputCT == "xml":
            builder = XMLBuilder()
            elements = builder.createElementsWithTextNodes(nick = nick, password = password)
            builder.appendListOfElementsToElement(builder.root(), elements)
            body = builder.toxml()
        else:
            body = JSONBuilder.getJSONObj(nick = nick, password = password)
            
        response, content = self.makeRequest(url, method = "POST", body = body, inputCT = inputCT)
        self.headers = response
        return content
