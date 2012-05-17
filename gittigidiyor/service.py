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
import httplib2
import time
import hashlib
import datetime
from provider import ProviderInterface

class Service(ProviderInterface):
    """
    Base class for Gittigidiyor API services. Each service has a name like 'application' Service.
    
    Some of them are seperated by their accessType like anonymous or individual. But it does not matter..
    """
    def __init__(self, serviceName, auth):
        """
        Base Constructor.
        """
        ProviderInterface.__init__(self, auth = auth)
        
        self.serviceName = serviceName
        """
        Service name for the service.
        """

    def signature(self, timestampString):
        """
        Generates a signature with the given timestamp, api key and the application secret.
        Timestamp must be a Unix-timestamp since Epoch.
        
        The resulting string is the md5 hexdigest of the appended api key, secret key and
        the timestamp.
        
        input: string
        
        output: string
        
        Example: sig = self.signature('1278338740580')
        
        print sig
                 
        f52e875b83f4f119828b53e108e4923e
        """
        return hashlib.md5(self.auth.key + self.auth.secret + timestampString).hexdigest()

    def createTimeStamp(self):
        """
        Returns a unix-timestamp since Epoch.
        output: string
        """
        now = time.time()
        timeSplitted = repr(now).split(".")
        first = float(timeSplitted[0])
        second = float("0." + timeSplitted[1])
        rounded = round((first + second) * 100.0)
        return "%d0" % rounded
    
    def makeRequest(self, url, method = "GET", body = None, headers = {}, inputCT = "xml"):
        """
        Performs an HTTP request with the given url..
        Extra parameters such as HTTP method, HTTP body, HTTP headers and the HTTP content type
        can be given, and they are set for the request before it is fired.
        
        'InputCT' parameter must only be either 'xml' or 'json'.
        
        Credentials for HTTP authentication is also included in this method.
        """
        # Create an Http instance..
        service = httplib2.Http()
        # Include the credientials for Basic Authentication..
        service.add_credentials(self.auth.username, self.auth.password)
        # Define the content type. Can be xml or json..
        contentType = "application/%s" % inputCT
        # Update the headers according to the input content type..
        headers.update({"Content-type": contentType})
        # Perform the HTTP request!
        response, content = service.request(url, method = method, body = body, headers = headers)
        # Return the response..
        return response, content
