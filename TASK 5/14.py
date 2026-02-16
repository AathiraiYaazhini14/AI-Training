from abc import ABC, abstractmethod

class AuthMethod(ABC):
    @abstractmethod
    def validate(self, credentials):
        pass


class PasswordAuth(AuthMethod):
    def validate(self, credentials):
        return credentials == "admin123"


class OTPAuth(AuthMethod):
    def validate(self, credentials):
        return credentials == "0000"


if __name__ == "__main__":
    methods = [PasswordAuth(), OTPAuth()]
    for method in methods:
        print(method.validate("admin123"))
