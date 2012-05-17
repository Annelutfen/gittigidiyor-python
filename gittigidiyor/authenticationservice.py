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

class AuthenticationService(Service):
    """
    This class represents the Authentication Service of the GittiGidiyor RESTLIKE API.
    """
    def __init__(self, auth):
        """
        Base Constructor. \n
        auth = Auth(username = 'testuser', password = 'testpassword', key = 'apikey', secret = 'apisecret') \n
        authenticationApi = AuthenticationService(auth)
        """
        Service.__init__(self, "authentication", auth)
        self.headers = None
        
    def createToken(self, inputCT, outputCT, lang):
        """
        Performs the 'createToken' API method for the Authentication Service API of Gittigidiyor. \n
        inputCT: output content type (xml or json) \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en' \n
        """
        url = "https://dev.gittigidiyor.com/listingapi/rlws/community/auth?method=createToken&outputCT=%s&inputCT=%s&apiKey=%s&sign=%s&time=%s&lang=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, inputCT, self.auth.key, signature, timestamp, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def getLoginURL(self, tokenId, redirectUrl):
        """
        Outputs the login url where the user grants permission to his GittGidiyor.com profile.
        """
        url = "http://dev.gittigidiyor.com/api/login.gg?apiKey=%s&sign=%s&time=%s&tokenId=%s&redirectUrl=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (self.auth.key, signature, timestamp, tokenId, redirectUrl)
        return url
