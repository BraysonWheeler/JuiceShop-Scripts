from abc import ABC, abstractmethod
import requests


class IRequest(ABC):
    """ Request Interface """

    @abstractmethod
    def get()-> requests:
        pass


class IPost(IRequest):
    """ Interface if a post and GET is made"""

    @abstractmethod
    def post()-> requests:
        pass


class SecurityQuestion(IRequest):
    """ Sends request to SecurityQuestion """

    def __init__(self, email, ip, headers) -> None:
        self.email = email
        self.ip = ip
        self.headers = headers

    def get(self) -> requests:
        return requests.get('http://%s/rest/user/security-question?email=%s' % (self.ip, self.email), headers=self.headers)
    

class RequestFactory:
    """ Class for deciding what type of Request to create """
    def send(context, email, ip, headers) -> requests:
        if context == 'securityquestion':
            return SecurityQuestion(email, ip, headers).get()

        

