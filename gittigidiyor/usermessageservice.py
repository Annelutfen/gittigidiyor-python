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

class UserMessagesService(Service):
    """
    This class represents the UserMessage Service of the GittiGidiyor RESTLIKE API.
    """
    def __init__(self, auth):
        """
        Base Constructor. \n
        auth = Auth(username = 'testuser', password = 'testpassword', key = 'apikey', secret = 'apisecret') \n
        usermessageApi = UserMessageService(auth)
        """
        Service.__init__(self, "usermessages", auth)
        self.headers = None

    def getInboxMessages(self, sessionId, startOffSet, rowCount, newOnly, outputCT, lang):
        """
        Performs the 'getInboxMessages' API method for the User Message Service API of Gittigidiyor.\n
        sessionId: session key fo the logged in user. \n
        startOffSet: is the offset in which city we start counting from. \n
        rowCount: is the number of how many cities will be fetched. \n
        newOnly: if True, only unread messages are fetched. \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en'\n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/community/message?method=getInboxMessages&outputCT=%s&apiKey=%s"
        url += "&sign=%s&time=%s&sessionId=%s&startOffSet=%d&rowCount=%d&unread=%s&lang=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        if newOnly:
            newOnly = "true"
        else:
            newOnly = "false"
        url = url % (outputCT, self.auth.key, signature, timestamp, sessionId, startOffSet, rowCount, newOnly, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content

    def sendNewMessage(self, sessionId, to, title, message, sendCopy, inputCT, outputCT, lang):
        """
        Performs the 'sendNewMessage' API method for the User Message Service API of Gittigidiyor.\n
        sessionId: session key for the logged in user. \n
        to: the message goes to whom. \n
        title: title of the message. \n
        message: body of the message. \n
        sendCopy: if True, the copy of the message is emailed to the sender. \n
        inputCT: output content type (xml or json) \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en'\n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/community/message?method=sendNewMessage&outputCT=%s&inputCT=%s&apiKey=%s&sign=%s&time=%s&sessionId=%s&lang=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, inputCT, self.auth.key, signature, timestamp, sessionId, lang)

        if sendCopy:
            sendCopy = "true"
        else:
            sendCopy = "false"

        if inputCT == "xml":
            builder = XMLBuilder()
            elements = builder.createElementsWithTextNodes(to = to, title = title, messageContent = message, sendCopy = sendCopy)
            builder.appendListOfElementsToElement(builder.root(), elements)
            body = builder.toxml()
        else:
            builder = JSONBuilder()
            body = JSONBuilder.getJSONObj(to = to, title = title, messageContent = message, sendCopy = sendCopy)

        response, content = self.makeRequest(url, method = "POST", body = body, inputCT = inputCT)
        self.headers = response
        return content

    def getSendedMessages(self, sessionId, startOffSet, rowCount, outputCT, lang):
        """
        Performs the 'getSendedMessages' API method for the User Message Service API of Gittigidiyor.\n
        sessionId: session key fo the logged in user. \n
        startOffSet: is the offset in which city we start counting from. \n
        rowCount: is the number of how many cities will be fetched. \n
        outputCT: output content type (xml or json) \n
        lang: 'tr' or 'en'\n
        """
        url = "http://dev.gittigidiyor.com:8080/listingapi/rlws/community/message?method=getSendedMessages&outputCT=%s"
        url += "&apiKey=%s&sign=%s&time=%s&sessionId=%s&startOffSet=%d&rowCount=%d&lang=%s"
        timestamp = self.createTimeStamp()
        signature = self.signature(timestamp)
        url = url % (outputCT, self.auth.key, signature, timestamp, sessionId, startOffSet, rowCount, lang)
        response, content = self.makeRequest(url)
        self.headers = response
        return content
