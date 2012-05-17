# Bu kod calismayacak, mantigi anlamak icin yazildi.
from gittigidiyor.authenticationservice import *
from gittigidiyor.auth import *

if __name__ == "__main__":
    # HTTP Basic authentication credentials.. It blows up for the wrong credentials..
    auth = Auth("testuser", "testpassword", None, None)
    api = AuthenticationService(auth)
    result = api.createToken(inputCT = "xml", outputCT = "xml", lang = "tr")
    print result
    # Result icinden tokenId degerini bul ve;
    redirectUrl = "example.com"
    print api.getLoginURL(tokenId, redirectUrl)
