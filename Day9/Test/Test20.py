#authinterfaces
from abc import ABC,abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self):
        print("This is login from google auth")
    def logout(self):
        print("this is logout from google auth")

class FaceBookAuth(UserAuthentication):
    def login(self):
        print("This is of facebook login")

    def logout(self):
        print("This is of facebook logout")

googleObj = GoogleAuth()
googleObj.login()
googleObj.logout()
fbObj = FaceBookAuth()
fbObj.login()
fbObj.logout()