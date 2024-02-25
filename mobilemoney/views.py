import random
from django.shortcuts import render
import requests
import json
import uuid
import base64
from django.http import HttpResponse
# Create your views here.

def uuidGen():
    global referenceId
    referenceId = uuid.uuid4()
    # print(referenceId)
    referenceId =str(referenceId)
    # print(referenceId)
    # referenceId ='876c7f9f-c0c4-4bb4-8c2c-ba58a6b9d8a7'
    return referenceId
# referenceId = '9646621f-1bf2-4aa8-9fe1-207c2d578922'
# apiKey = '85a81350c0d74638b95f2aa1faefb707'
secondaryKey = '85d91a1d4a334d64a236ee154b9082ee'

def createapiuser(request):
    
    url = "https://sandbox.momodeveloper.mtn.com/v1_0/apiuser"
        

    payload = json.dumps({
    "providerCallbackHost": "https://webhook.site/252aa2b5-0655-448f-8d39-f43885f6798c"
    })
    headers = {
    'X-Reference-Id': referenceId,
    'Ocp-Apim-Subscription-Key': secondaryKey,
    'Content-Type': 'application/json',
    # 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6ImNiYTA5NjQwLTlmMjEtNDkyMC04Zjk4LTU5N2FkYTQwZTQ3OCIsImV4cGlyZXMiOiIyMDI0LTAyLTIzVDA2OjQ3OjQyLjk5NCIsInNlc3Npb25JZCI6ImUwMWQ4YzE4LThkZDktNDQzYi04ZTdmLTdiYmM5YWNhNDkwYSJ9.IaFKaKW3qvDTVWusDW8kVbolHx31uivDW0ORjER4UPlWlwtn6YirrttbAbeYPc5WlVx_cbFcYycgpNfNyoDxkWmZxLUGHqMwWMnU3UnCOWTqsF5oexoSMehKIM-LXTISn6pAIJUMl1TKpOQbzA1s77HRC_EBqGChzu2b-djCVUavOdvSiXk7u0FkeUwUK9LShk0jSizd6Rp8jykhYbiL9p_HHf-Cm6qQbfolCjPCExZWcgo0enL_bWZhMjU5VkPmsP6v27ShemKGTHaeH_7vn8zE9rIL4grbnyUbiMNGAM1evSTSDQWuHDlYXL5Lke9zq0hV5Yh2uqmAqBP4_b9xJQ'
    }
    # print(uuidGen())

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    # print(referenceId)

    return HttpResponse(response.text)


def createApiKey(request):
    createapiuser(request)
    url = "https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/{}/apikey".format( referenceId )
    print(url)
    payload = {}
    headers = {
    'Ocp-Apim-Subscription-Key': '85d91a1d4a334d64a236ee154b9082ee',
    # 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6ImNiYTA5NjQwLTlmMjEtNDkyMC04Zjk4LTU5N2FkYTQwZTQ3OCIsImV4cGlyZXMiOiIyMDI0LTAyLTIzVDA2OjQ3OjQyLjk5NCIsInNlc3Npb25JZCI6ImUwMWQ4YzE4LThkZDktNDQzYi04ZTdmLTdiYmM5YWNhNDkwYSJ9.IaFKaKW3qvDTVWusDW8kVbolHx31uivDW0ORjER4UPlWlwtn6YirrttbAbeYPc5WlVx_cbFcYycgpNfNyoDxkWmZxLUGHqMwWMnU3UnCOWTqsF5oexoSMehKIM-LXTISn6pAIJUMl1TKpOQbzA1s77HRC_EBqGChzu2b-djCVUavOdvSiXk7u0FkeUwUK9LShk0jSizd6Rp8jykhYbiL9p_HHf-Cm6qQbfolCjPCExZWcgo0enL_bWZhMjU5VkPmsP6v27ShemKGTHaeH_7vn8zE9rIL4grbnyUbiMNGAM1evSTSDQWuHDlYXL5Lke9zq0hV5Yh2uqmAqBP4_b9xJQ'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    # print(type(response.json()))
    # print(response.json()['apiKey'])

    if response.status_code == 201:
        response = response.json()
        apiKey = response['apiKey']
        print(apiKey)
        
    else:
        print('Failed to generate apikey')

    # print(response.text)
    # print(response.status_code)

    return apiKey




def getCreatedUser(request):
    createapiuser(request)

    url = "https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/{}".format( referenceId )

    payload = {}
    headers = {
    'Ocp-Apim-Subscription-Key': '85d91a1d4a334d64a236ee154b9082ee',
    # 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6ImNiYTA5NjQwLTlmMjEtNDkyMC04Zjk4LTU5N2FkYTQwZTQ3OCIsImV4cGlyZXMiOiIyMDI0LTAyLTIzVDA2OjQ3OjQyLjk5NCIsInNlc3Npb25JZCI6ImUwMWQ4YzE4LThkZDktNDQzYi04ZTdmLTdiYmM5YWNhNDkwYSJ9.IaFKaKW3qvDTVWusDW8kVbolHx31uivDW0ORjER4UPlWlwtn6YirrttbAbeYPc5WlVx_cbFcYycgpNfNyoDxkWmZxLUGHqMwWMnU3UnCOWTqsF5oexoSMehKIM-LXTISn6pAIJUMl1TKpOQbzA1s77HRC_EBqGChzu2b-djCVUavOdvSiXk7u0FkeUwUK9LShk0jSizd6Rp8jykhYbiL9p_HHf-Cm6qQbfolCjPCExZWcgo0enL_bWZhMjU5VkPmsP6v27ShemKGTHaeH_7vn8zE9rIL4grbnyUbiMNGAM1evSTSDQWuHDlYXL5Lke9zq0hV5Yh2uqmAqBP4_b9xJQ'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return HttpResponse(response.text)


def generateAccessToken(request):
    # createApiKey(request)

    # print (createApiKey(request))

    url = "https://sandbox.momodeveloper.mtn.com/collection/token/"

    userpass = uuidGen() + ':' + createApiKey(request)
    
    # userpass = referenceId + ':' + apiKey
    encoded_u = base64.b64encode(userpass.encode()).decode()
    payload = {}
    headers = {
    'Ocp-Apim-Subscription-Key': '85d91a1d4a334d64a236ee154b9082ee',
    'Authorization': 'Basic %s' % encoded_u
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    if response.status_code == 200:
        response = response.json()
        access_token = response['access_token']
        # print(access_token)
    else:
        print('failed to generate access token')
    return access_token


def requestPay(request):

    url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"
    
    cost = "50.0"
    phone = 6774341654
    eternalId = random.randint(10000000, 99999999)
    access_token = generateAccessToken(request)
    print(referenceId)
    print(access_token)

    payload = json.dumps({
    "amount": cost,
    "currency": "EUR",
    "externalId": 'kdjdjd95858s',
    "payer": {
        "partyIdType": "MSISDN",
        "partyId": phone
    },
    "payerMessage": "Ticket payment",
    "payeeNote": "bus Ticket pay"
    })
    headers = {
    'X-Reference-Id': referenceId,
    'X-Target-Environment': 'sandbox',
    'Ocp-Apim-Subscription-Key': '85d91a1d4a334d64a236ee154b9082ee',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer %s' % access_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    if response.status_code == 202:
        # response = response.json()
        print('REQUEST SUCCESFULL')
        print(response)
        # access_token = response['access_token']
        # print(access_token)
    else:
        print('failed to generate access token')
    # return access_token

    return HttpResponse(response.text)


def requestToPayStatus(request):
    refId = 'getalredy gen and saved in db'
    # access_token should be same as that generated with the ref id here saved in db
    access_token = generateAccessToken(request)

    print(access_token)

    url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay/{}".format(referenceId)

    payload = {}
    headers = {
    'Ocp-Apim-Subscription-Key': '85d91a1d4a334d64a236ee154b9082ee',
    'X-Target-Environment': 'sandbox',
    'Authorization': 'Bearer %s' % access_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    if response.status_code == 200:
        print('paid')
    else:
        print('unpaid')
    return HttpResponse(response.status_code)