# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:37:39 2024

@author: Serkan YILDIZ yildiz@serkan.net

"""


import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "http://standards.ieee.org/develop/regauth/oui/oui.txt"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def ParseIEEEMac():

    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        data = response.text
    else:
        print("Status code:", response.status_code)

    IEEEMac = []
    Lines = data.splitlines()
    for line in Lines:
        if "(hex)" in line:
            Mac_OUI = line[0:8]
            Company = line[18:]
            IEEEMac.append([Mac_OUI, Company])

    return IEEEMac

Mac_Vendors_List=ParseIEEEMac()

print(Mac_Vendors_List)
