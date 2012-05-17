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

class CargoService(Service):
    """
    This class represents the Cargo Service of the GittiGidiyor RESTLIKE API.
    """
    def __init__(self, auth):
        """
        Base Constructor. \n
        auth = Auth(username = 'testuser', password = 'testpassword', key = 'apikey', secret = 'apisecret') \n
        cargoApi = CargoService(auth)
        """
        Service.__init__(self, "cargo", auth)
        self.headers = None

    def getCargoInformation(self, sessionId, saleCode, outputCT, lang):
        """
        Performs the 'getCargoInformation' API method for the Cargo Service API of Gittigidiyor. \n
        sessionId: session key fo the logged in user. \n
        saleCode: sale code. \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en' \n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/community/cargo?method=getCargoInformation"
        url += "&outputCT=%s&apiKey=%s&sign=%s&time=%s&sessionId=%s&lang=%s&saleCode=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, self.auth.key, signature, timestamp, sessionId, lang, saleCode)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def sendCargoInformation(self, sessionId, saleCode, cargoPostCode, cargoCompany, cargoBranch, followUpUrl, userType, inputCT, outputCT, lang):
        """
        Performs the 'sendCargoInformation' API method for the Cargo Service API of Gittigidiyor. \n
        sessionId: session key fo the logged in user. \n
        saleCode: sale code. \n
        cargoPostCode: Cargo number. \n
        cargoCompany: cargo company such as yurtici, MNG.. \n
        cargoBranch: township for the cargo branch such as Taksim, Kadikoy. \n
        followUpUrl: cargo external url. \n
        userType: Determines the user. Can be 'A' for all, 'S' for seller, 'B' for buyer or 'N' for none. \n
        inputCT: input content type (xml or json) \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en' \n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/community/cargo?method=sendCargoInformation"
        url += "&outputCT=%s&inputCT=%s&apiKey=%s&sign=%s&time=%s&sessionId=%s&lang=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, inputCT, self.auth.key, signature, timestamp, sessionId, lang)

        if inputCT == "xml":
            builder = XMLBuilder()
            elements = builder.createElementsWithTextNodes(saleCode = saleCode, cargoPostCode = cargoPostCode,
                                                           cargoCompany = cargoCompany, cargoBranch = cargoBranch,
                                                           followUpUrl = followUpUrl, userType = userType)
            builder.appendListOfElementsToElement(builder.root(), elements)
            body = builder.toxml()
        else:
            builder = JSONBuilder()
            body = JSONBuilder.getJSONObj(saleCode = saleCode, cargoPostCode = cargoPostCode,
                                          cargoCompany = cargoCompany, cargoBranch = cargoBranch,
                                          followUpUrl = followUpUrl, userType = userType)

        response, content = self.makeRequest(url, method = "POST", body = body, inputCT = inputCT)
        self.headers = response
        return content
