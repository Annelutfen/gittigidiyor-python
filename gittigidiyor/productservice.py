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

class ProductService(Service):
    """
    This class represents the Product Service of the GittiGidiyor RESTLIKE API.
    """
    def __init__(self, auth):
        """
        Base Constructor. \n
        auth = Auth(username = 'testuser', password = 'testpassword', key = 'apikey', secret = 'apisecret') \n
        productApi = ProductService(auth)
        """
        Service.__init__(self, "product", auth)
        self.headers = None

    def getProducts(self, sessionId, startOffSet, rowCount, status, withData, outputCT, lang):
        """
        Performs the 'getProducts' API method for the Product Service API of Gittigidiyor. \n
        sessionId: session key fo the logged in user. \n
        startOffSet: is the offset in which city we start counting from. \n
        rowCount: is the number of how many cities will be fetched. \n
        status: status of the user's products. Can be; \n
        A - Aktif Şatışlar
        
        L - Yeni Listelenenler
        
        S - Satılan Ürünler
        
        U - Satılmayan Ürünler
        
        R - Yeniden Listelenenler
        
        withData: if True, the product details are also fetched. \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en' \n
        """
        url = "https://dev.gittigidiyor.com/listingapi/rlws/community/product?method=getProducts"
        url += "&outputCT=%s&apiKey=%s&sign=%s&time=%s&sessionId=%s&lang=%s&startOffSet=%d&rowCount=%d&status=%s&withData=%s"
        if withData:
            withData = "true"
        else:
            withData = "false"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, self.auth.key, signature, timestamp, sessionId, lang, startOffSet, rowCount, status, withData)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def getProduct(self, sessionId, productId, outputCT, lang):
        """
        Performs the 'getProduct' API method for the Product Service API of Gittigidiyor.
        """
        url = "https://dev.gittigidiyor.com/listingapi/rlws/community/product?method=getProduct&outputCT=%s&apiKey=%s&sign=%s&time=%s&sessionId=%s&lang=%s&productId=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, self.auth.key, signature, timestamp, sessionId, lang, productId)
        response, content = self.makeRequest(url)
        self.headers = response
        return content
