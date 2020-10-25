import hashlib, sys, time, os

def Get_Hash(filepath) -> str:
        hash = ""
        BUF_SIZE = 65536
        md5 = hashlib.md5()
        try:
            with open(filepath, "rb") as f:
                while True:
                    data = f.read(BUF_SIZE)
                    if not data:
                        break
                    md5.update(data)
            return (md5.hexdigest())
        except Exception as e:
            return 
            (print("[!] Hash Calculating Failed!"), 
            time.sleep(3), 
            os._exit(0)
            )
try:
    filepath = sys.argv[1]
except:
    filepath = input('File Path -> ')

print("Hash: {}".format(Get_Hash(filepath)))
input()
