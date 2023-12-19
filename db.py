import requests

x = "DOT033771732" #input("Enter UID: ")
burp0_url = f"https://auth.dotpay.africa:443/v1/auth/onboard/docs/{x}"
burp0_headers = {"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarySNA2gOIBsRDsrQHa", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36", "Serialnumber": "mobile-app", "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJkYW5pZWxpeW9ndW4xMTFAZ21haWwuY29tIiwidXNlcklkIjoiRE9UMDMzNzcxNzMyIiwibWVyY2hhbnRJZCI6IjA0MTIzNDU2NzgiLCJlbWFpbCI6ImRhbmllbGl5b2d1bjExMUBnbWFpbC5jb20iLCJmdWxseUF1dGhlbnRpY2F0ZWQiOnRydWUsInJvbGUiOlsiUk9MRV9QUkVfQUdFTlQiXSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QUkVfQUdFTlQiXSwiaWF0IjoxNzAyOTM2MDg2LCJleHAiOjE3MDI5NTQwODZ9.VKEfs6trcUmV2J_yrVNWU_Xnzthn8H05Bt0KG3Ywb6EPHjHB4CHBZikOEuMEd86Bkf2bLZzErjz2RUVa2ylT1Q", "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/4.9.1", "Connection": "close"}
data = """------WebKitFormBoundarySNA2gOIBsRDsrQHa
Content-Disposition: form-data; name="IdFile"

undefined
------WebKitFormBoundarySNA2gOIBsRDsrQHa
Content-Disposition: form-data; name="nokIdFile"

undefined
------WebKitFormBoundarySNA2gOIBsRDsrQHa
Content-Disposition: form-data; name="passportPhoto"

undefined
------WebKitFormBoundarySNA2gOIBsRDsrQHa
Content-Disposition: form-data; name="utilityFile"

undefined
------WebKitFormBoundarySNA2gOIBsRDsrQHa--"""
resp = requests.get(burp0_url, headers=burp0_headers, data=data)
print(resp.text)
