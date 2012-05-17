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

class ApplicationService(Service):
    """
    This class represents the Application Service of the GittiGidiyor RESTLIKE API.
    """
    def __init__(self, auth):
        """
        Base Constructor. \n
        auth = Auth(username = 'testuser', password = 'testpassword', key = None, secret = None) \n
        applicationApi = ApplicationService(auth)
        """
        Service.__init__(self, "application", auth)
        self.headers = None
        
    def createApplication(self, developerId, name, description, accessType, appType, descDetail, inputCT, outputCT, lang):
        """
        Performs the 'createApplication' API method for the Application Service API of Gittigidiyor.
        
        developerId: is the developer id that determines which developer is going to perform this request.
        
        name: is the application's name.
        
        description: is the description of the application
        
        accessType: must be 'I' for individual access, 'C' for community access.
        
        appType: take a look at - http://dev.gittigidiyor.com/servisler/createApplication-ApplicationService-soap-anonymous
        
        descDetail: if appType is 'O', you can input some text here for details.. otherwise leave it empty.
        
        inputCT: input content type
        
        outputCT: output content type
        
        lang: 'tr' for Turkish, 'en' for English
        """
        if not inputCT in ("xml", "json"):
            raise Exception("Gondereceginiz veriyi yalnizca xml ya da json tipinde gonderebilirsiniz.")
        # Build up the HTTP POST body..
        if inputCT == "xml":
            builder = XMLBuilder()
            elements = builder.createElementsWithTextNodes(developerId = developerId, name = name,
                                                           description = description,accessType = accessType,
                                                           appType = appType, descDetail = descDetail)
            builder.appendListOfElementsToElement(builder.root(), elements)
            body = builder.toxml()
        else: # json
            body = JSONBuilder.getJSONObj(developerId = developerId, name = name, description = description,
                                          accessType = accessType, appType = appType, descDetail = descDetail)

        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/application?method=createApplication&outputCT=%s&inputCT=%s&lang=%s"
        url = url % (outputCT, inputCT, lang)
        response, content = self.makeRequest(url, method = "POST", body = body, inputCT = inputCT)
        self.headers = response
        return content

    def deleteApplication(self, developerId, apikey, outputCT, lang):
        """
        Performs the 'deleteApplication' API method for the Application Service API of Gittigidiyor.
        
        http://dev.gittigidiyor.com/metotlar/deleteApplication-ApplicationService-soap-anonymous
        
        developerId: is the developer id that determines which developer is going to perform this request.
        
        apikey: the key of the application to be deleted.
        
        outputCT: output content type
        
        lang: 'tr' for Turkish, 'en' for English
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/application?method=deleteApplication&outputCT=%s&developerId=%s&apiKey=%s&lang=%s"
        url = url % (outputCT, developerId, apikey, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def getApplicationList(self, developerId, outputCT, lang):
        """
        Performs the 'getApplicationList' API method for the Application Service API of Gittigidiyor.
        
        http://dev.gittigidiyor.com/metotlar/getApplicationList-ApplicationService-soap-anonymous
        
        developerId: is the developer id that determines which developer is going to perform this request.
        
        outputCT: output content type
        
        lang: 'tr' for Turkish, 'en' for English        
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/anonymous/application?method=getApplicationList&outputCT=%s&developerId=%s&lang=%s"
        url = url % (outputCT, developerId, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content
