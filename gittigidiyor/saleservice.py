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

class SaleService(Service):
    """
    This class represents the Sale Service of the GittiGidiyor RESTLIKE API.
    """
    def __init__(self, auth):
        """
        Base Constructor. \n
        auth = Auth(username = 'testuser', password = 'testpassword', key = 'apikey', secret = 'apisecret') \n
        saleApi = SaleService(auth)
        """
        Service.__init__(self, "sale", auth)
        self.headers = None

    def getSales(self, sessionId, startOffSet, rowCount, withData, byStatus, byUser, outputCT, orderBy, orderType, lang):
        """
        Performs the 'getSales' API method for the Sale Service API of Gittigidiyor.\n
        sessionId: session key fo the logged in user. \n
        startOffSet: is the offset in which city we start counting from. \n
        rowCount: is the number of how many cities will be fetched. \n
        withData: if True, the sale details are also fetched. \n
        byStatus: http://dev.gittigidiyor.com/metotlar/getSales-SaleService-rlws-community. \n
        byUser: http://dev.gittigidiyor.com/metotlar/getSales-SaleService-rlws-community. \n
        outputCT: output content type (xml or json) \n
        orderBy: http://dev.gittigidiyor.com/metotlar/getSales-SaleService-rlws-community \n
        orderType: http://dev.gittigidiyor.com/metotlar/getSales-SaleService-rlws-community \n
        lang: 'tr' or 'en' \n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/community/sale?method=getSales&outputCT=%s"
        url += "&apiKey=%s&sign=%s&time=%s&sessionId=%s&lang=%s&startOffSet=%d&rowCount=%d&withData=%s"
        url += "&byStatus=%s&byUser=%s&orderBy=%s&orderType=%s"
        if withData:
            withData = "true"
        else:
            withData = "false"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, self.auth.key, signature, timestamp, sessionId, lang,
                     startOffSet, rowCount, withData, byStatus, byUser, orderBy, orderType)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def getSale(self, sessionId, saleCode, outputCT, lang):
        """
        Performs the 'getSale' API method for the Sale Service API of Gittigidiyor. \n
        sessionId: session key fo the logged in user. \n
        saleCode: sale code. \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en' \n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/community/sale?method=getSale&outputCT=%s&apiKey=%s&sign=%s&time=%s&sessionId=%s&lang=%s&saleCode=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, self.auth.key, signature, timestamp, sessionId, lang, saleCode)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def giveRateAndComment(self, sessionId, productId, rate, comment, userType, inputCT, outputCT, lang):
        """
        Performs the 'giveRateAndComment' API method for the Sale Service API of Gittigidiyor.\n
        sessionId: session key fo the logged in user. \n
        productId: product unique id. \n
        rate: rate for the product. domain: [1,5]
        comment: comment for the given sale..
        userType: Determines the user. Can be 'A' for all, 'S' for seller, 'B' for buyer or 'N' for none. \n
        inputCT: input content type (xml or json) \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en' \n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/community/sale?method=giveRateAndComment&outputCT=%s"
        url += "&inputCT=%s&apiKey=%s&sign=%s&time=%s&sessionId=%s&lang=%s&userType=%s&productId=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, inputCT, self.auth.key, signature, timestamp, sessionId, lang, userType, productId)
        
        if inputCT == "xml":
            builder = XMLBuilder()
            elements = builder.createElementsWithTextNodes(rate = rate, comment = comment)
            builder.appendListOfElementsToElement(builder.root(), elements)
            body = builder.toxml()
        else:
            builder = JSONBuilder()
            body = JSONBuilder.getJSONObj(rate = rate, comment = comment)
            
        response, content = self.makeRequest(url, method = "POST", body = body, inputCT = inputCT)
        self.headers = response
        return content

    def replySaleComment(self, sessionId, productId, comment, userType, inputCT, outputCT, lang):
        """
        Performs the 'replySaleComment' API method for the Sale Service API of Gittigidiyor.\n
        sessionId: session key fo the logged in user. \n
        productId: product unique id. \n
        comment: comment for the given sale..
        userType: Determines the user. Can be 'A' for all, 'S' for seller, 'B' for buyer or 'N' for none. \n
        inputCT: input content type (xml or json) \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en' \n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/community/sale?method=replySaleComment&outputCT=%s"
        url += "&inputCT=%s&apiKey=%s&sign=%s&time=%s&sessionId=%s&lang=%s&userType=%s&productId=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, inputCT, self.auth.key, signature, timestamp, sessionId, lang, userType, productId)
        if inputCT == "xml":
            builder = XMLBuilder()
            elements = builder.createElementsWithTextNodes(comment = comment)
            builder.appendListOfElementsToElement(builder.root(), elements)
            body = builder.toxml()
        else:
            builder = JSONBuilder()
            body = JSONBuilder.getJSONObj(comment = comment)

        response, content = self.makeRequest(url, method = "POST", body = body, inputCT = inputCT)
        self.headers = response
        return content
