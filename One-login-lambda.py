import json
import boto3
import requests
from requests.auth import HTTPBasicAuth

ssm=boto3.client('ssm')

subDomain = "dimons"
#subDomain = os.environ(subDomain)
apiURL = "https://{}.onelogin.com/oidc/2/token/introspection".format(subDomain)
#apiURL= os.environ(apiURL)
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
# clientId = ssm.get_parameter(Name='OneLoginClientID', WithDecryption=True)
# clientSecret = ssm.get_parameter(Name='OneLoginClientSecret', WithDecryption=True)
clientId="6d1281e0-4f23-0139-97e2-0691d9562397184560"
clientSecret="73ea20f33b33efc32731d95bdd173d5220d7929a7c446a18dad36081aab84611"

token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpSY080bnhzNWpnYzhZZE43STJoTE80Vl9xbDFiZG9pTVhtY1lnSG00SHMifQ.eyJqdGkiOiI0MlUyYlZQUndqbXh4M0hjaVAzX1AiLCJzdWIiOiIxMjM3MTEwNTEiLCJpc3MiOiJodHRwczovL2RpbW9ucy5vbmVsb2dpbi5jb20vb2lkYy8yIiwiaWF0IjoxNjEzNjI0MzM5LCJleHAiOjE2MTM2Mjc5MzksInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdWQiOiI2ZDEyODFlMC00ZjIzLTAxMzktOTdlMi0wNjkxZDk1NjIzOTcxODQ1NjAifQ.fI6a-xXdiSSfOTRXjtyXySwhD8wxwOK3pOB97ym4lbTqUmRq2h7R_Dy2TzzJrGIYMCim3zPb9O9bWjMord6Com3eVyggBu6X9BGil08LC9V7B3ykUXZV1KC3Oopj9c3WroN36rBr4Fps4VXiWjjIA4tSSkz9a9BPUOXT6iJYbzxzrcWuzPP0OsTrH_E5VvXOH4a5I0WJZHf-rttFK1HEM2hMVA1E3UsiEXtKKPY3AhIbXYXszlMghvB98qLm-t1FWcG48Z27cIXdLdy4F1mV82fphvZQQY2RLc5X_2p5vLxQ6D42_c5FY15cqrICsxZoWyX985rWL4YTw2CygyI5IA"


# first push to git
# def lambda_handler(event, context):
#     # TODO implement
#     print(event)
#     token = event['authorizationToken']
#     print(token)

body = {
    "token" : token,
    "token_type_hint" : "access_token"
}
response = requests.post(apiURL, headers=headers, data=body, auth = HTTPBasicAuth(clientId, clientSecret))
responseText = response.text
print(responseText)
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
