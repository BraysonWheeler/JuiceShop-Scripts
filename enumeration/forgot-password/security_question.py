from file_factory import GetContentsOfFile
from request_factory import RequestFactory


def main():
    ip = GetContentsOfFile("list.txt", 'ip').get()
    email_list = GetContentsOfFile("list.txt", 'emails').get()
    valid_emails = []

    Request = RequestFactory

    for email in email_list:
        Response = Request.send('securityquestion', email, ip, {'Accept' : 'application/json'})
        if len(Response.json()): valid_emails.append([email, Response.json()])
    
    print(valid_emails)


if __name__ =="__main__":
    main()