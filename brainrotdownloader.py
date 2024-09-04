import datetime
import json
import requests
from urllib.request import urlretrieve, HTTPHandler, build_opener, install_opener
from urllib.error import HTTPError
from random import randint
from os.path import isfile

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

class MyUserAgentHTTPHandler(HTTPHandler):
    def http_request(self, req):
        req.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0"
        return super().http_request(req)

install_opener(build_opener(MyUserAgentHTTPHandler()))

brainrots = []

with open("brainrots.txt") as file:
    for line in file:
        brainrots.append(line)
        
        response = requests.post("https://api.cobalt.tools/api/json", json={"url": line}, headers=headers)
        
        if response.ok:
            response_json = response.json()
            
            if response_json["status"] == "stream":
                with requests.get(response_json["url"], stream=True, headers=headers) as response:
                    response.raise_for_status()
                    
                    while True:
                        filepath = f"brainrot/{randint(1000000, 9999999)}.mp4"
                        
                        if not isfile(filepath):
                            break
                    
                    with open(filepath, "wb") as file:
                        for chunk in response.iter_content():
                            if chunk:
                                file.write(chunk)
    
now = datetime.datetime.now()

with open(f"old_brainrots/brainrots{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}.txt", "w") as backup_file:
    backup_file.write("".join(brainrots))
        
open("brainrots.txt", "w").close()