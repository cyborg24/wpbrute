import requests, json, time
from functions import getTx
import multiprocessing as mp
import time

bearer = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IlVTRVIiLCJpYXQiOjE2ODA4MDc2MDAsInN1YiI6IjIyMjM5NyIsImV4cCI6MTY4MDg5NDAwMH0.m9Vej_o4K_3Rnb4JXw2ELe_wSk1fZOd_JioUD8WLHW8"

#def mainProg(m,n,p,fn):
fn = "All-new-bal.txt"
with open("BIG/All-300000.txt", "r") as handle:
    lines = handle.readlines()
i = 1
for line in lines:
    userid = line.split("/")
    userid = userid[0]
    try:
        url = f'https://business-banking.kudi.ai/user/{userid}'
        mheaders = {"Authorization": bearer}
        x = requests.get(url, headers = mheaders)
        resp = x.text
        resp = resp[27:46]
        #print(resp)
        if resp == "User does not exist":
            print(f"process: 1=>>{userid}==> user does not exist")
        else:
            print(x.text)
            json_data = json.loads(x.text)
            try:
                id2 = json_data['data']['parentBusiness']
            except:
                #time.sleep(2)
                id2 = json_data['data']['parentBusiness'] or 10841
            """
            url2 = f'https://business-banking.kudi.ai/business/{id2}/get-wallet-and-ledger-balance'
            x2 = requests.get(url2, headers = mheaders)
            json_data2 = json.loads(x2.text)
            """
            #try:
            """
                balance = json_data2['data']['ledgerBalance']
            """
            balance = getTx(id2)
            #print(balance)
            #exit()
            print(f"process: 1=>>Balance for {id2}==>\n {balance}")
            #except:
            #print("No Business Found For UID!")
            #balance = 0.0
            #time.sleep(2)
            if float(balance) > 0.0 and json_data['data']['registrationId'] != None:
                with open("BIG/"+fn, "a") as handle:
                    handle.write(str(json_data['data']['registrationId']) + "/" +str(json_data['data']['id']) + "/" + str(id2) + " - " + str(balance) + "\n")
                    print("\n ID recorded")

    except:
        pass