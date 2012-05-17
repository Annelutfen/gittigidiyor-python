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
from xml.dom import minidom

class XMLBuilder(minidom.Document):
    """
    This class intends to wrap around the Document class which is inside the minidom library,
    and provides some utility functions to build up XML document easily.
    """
    def __init__(self, tag = "request"):
        minidom.Document.__init__(self)
        self.rootElement = self.createElement(tag)
        self.appendChild(self.rootElement)

    def root(self):
        """
        Gets the root element which is at the top of Dom hierarchy.
        """
        return self.rootElement

    def createElementWithTextNode(self, tagName, nodeValue):
        """
        Creates a dom element with the given tag name and the node value.
        
        input: string, string
        
        output: DOM Element
        
        Example: element = self.createElementWithTextNode('rate', '5')
        
        print element.toxml()
        
        '<rate>5</rate>'
        """
        nodeValue = True and nodeValue or ""
        element = self.createElement(str(tagName))
        node = self.createTextNode(str(nodeValue))
        element.appendChild(node)
        return element

    def createElementsWithTextNodes(self, **kwargs):
        """
        Creates a list of DOM Element instances with the given unlimited parameters.
        
        input: string, string ...
        
        output: [DOM Element, DOM Element, ...]
        """
        return [self.createElementWithTextNode(k, v) for k, v in kwargs.items()]

    def appendListOfElementsToElement(self, element, elements):
        """
        Appends list of DOM elements to the given DOM element as a child.
        
        input: DOM Element, [DOM Element, DOM Element, ...]
        
        output: NULL
        """
        for ele in elements:
            element.appendChild(ele)

    def __unicode__(self):
        return self.toxml()
    
    @staticmethod
    def get_data(xml, s):
        """
        Static method for traversing and getting the text value for
        the given tag name 's' inside the DOM tree 'xml'..
        """
        try:
            document = minidom.parseString(str(xml))
            a = document.getElementsByTagName(s)[0]
            return a.childNodes[0].data
        except:
            return ""
