from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/postmaster.readonly']

def main():
    """Shows basic usage of the PostmasterTools v1beta1 API.
    Prints the visible domains on user's domain dashboard in https://postmaster.google.com/managedomains.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)



    service = build('gmailpostmastertools', 'v1beta1', credentials=creds)

    #for key, value in service.__dict__.items():
    #    print(f"key: {key}")
    #    print(f"value: {value}")

    domains_resource = service.domains()

    domains = domains_resource.list().execute()
    if not domains:
        print('No domains found.')
    else:
        print('Domains:')
        for domain in domains['domains']:
            name = domain["name"]
            create_time = domain["createTime"]
            permission = domain["permission"]
            print(f"    domain.name: {name}")
            print(f"    domain.createTime: {create_time}") 
            print(f"    domain.permission: {permission}") 

    try:
        traffic_stats = domains_resource.trafficStats().list(parent = 'domains/kylemoulder.com').execute()
        print("Found traffic stats!")
        print(traffic_stats)
    except Exception as e:
        print("No traffic stats found")
        print(e)

if __name__ == '__main__':
  main()
