# Bu kod calismayacak, mantigi anlamak icin yazildi.
from gittigidiyor.applicationservice import *
from gittigidiyor.auth import *

if __name__ == "__main__":
    # HTTP Basic authentication credentials.. It blows up for the wrong credentials..
    auth = Auth("testuser", "testpassword", None, None)
    api = ApplicationService(auth)
    result = api.createApplication("testdeveloper", "Test Application", "This is the test application",
                                   "C", "W", "", "xml", "xml", "tr")
    print result
