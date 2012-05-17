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

class ProviderInterface(object):
    """
    Base Interface for GittiGidiyor RESTLIKE API.
    Every service provider must implement this interface. Services can be anonymous
    or community services. Services that implements this interface are;\n
    * Application service
    
    * Category service
    
    * City service
    
    * Developer service
    
    * Catalog service
    
    * Search service
    
    * Product service
    
    * Sale service
    
    * Cargo service
    
    * User messages service
    
    * Authentication service 
    """
    def __init__(self, auth):
        self.auth = auth
        """
        Auth object for the service..
        """

    def makeRequest(self, url, method = "GET", body = None, headers = None):
        """
        Performs an HTTP(S) request with Basic Authentication included..
        It returns an HTTP response with headers.
        """
        pass
    
    def createTimeStamp(self):
        """
        Creates a timestamp string as the server understands.
        Anonymous services doesn't need to implement this method.
        Because they don't need a timestamp to perform an HTTP request.
        output: string
        """
        pass

    def signature(self, timestampString):
        """
        Creates an API signature with the given timestamp string.
        Anonymous services don't need to implement this method.
        Because they don't need a timestamp to perform an HTTP request.
        output: string
        """
        pass
