import json
import requests
import os
import time
from tqdm import tqdm

DATA_DIR = './data/editions'
ABLO_BASE = "https://api-brucknerlex.acdh.oeaw.ac.at/article"
os.makedirs(DATA_DIR, exist_ok=True)

headers = {'Accept': 'application/json'}

url = f"{ABLO_BASE}?max=5000"
print("download article list")
response = requests.request("GET", url, headers=headers)
data = response.json()
with open('./data/arcticles.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, ensure_ascii=False))

headers = {'Accept': 'application/xml'}

print("start downloading single XMLs")
for x in tqdm(data['results']['article'], total=int(data['results']['total'])):
    url = f"{ABLO_BASE}/{x['id']}"
    response = requests.request("GET", url, headers=headers)
    with open(f"{DATA_DIR}/{x['id']}.xml", 'w', encoding="utf-8") as f:
        f.write(response.text)
    time.sleep(0.2)
print("DONE")
