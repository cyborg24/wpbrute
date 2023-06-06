import fast_luhn as fl


for line in range(1000000000,9999999999):
    data = f"539983{line}"
    res = fl.validate(data)
    print (f"{line} : {data} ==> {res}")
    if res == True:
        with open("aacinfo.txt", "a") as handle:
            handle.write(data + "\n")
            print (f"written")