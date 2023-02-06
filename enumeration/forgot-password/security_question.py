import requests
from get_contents import GetContentsOfFile


def main():
    ip = GetContentsOfFile("list.txt", 'ip').get()
    email_list = GetContentsOfFile("list.txt", 'emails').get()
    valid_emails = []
    for email in email_list:
        url = 'http://%s/rest/user/security-question?email=%s' % (ip, email)
        response = requests.get(url, headers= {'Accept' : 'application/json'})
        if (len(response.json()) > 0):
            valid_emails.append(email)

    
    print(valid_emails)
if __name__ =="__main__":
    main()