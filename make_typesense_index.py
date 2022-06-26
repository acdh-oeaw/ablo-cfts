import glob
import os

from acdh_cfts_pyutils import CFTS_COLLECTION
from acdh_tei_pyutils.tei import TeiReader
from tqdm import tqdm

files = glob.glob('./data/editions/*.xml')
schema_name = 'ablo'


records = []
for x in tqdm(files, total=len(files)):
    try:
        doc = TeiReader(x)
    except:
        continue
    record = {
        'project': schema_name,
    }
    
    body = doc.any_xpath('.//tei:body')[0]
    record['rec_id'] = os.path.split(x)[-1]
    record['id'] = f"ABLO_{os.path.split(x)[-1].replace('.xml', '')}"
    record['resolver'] = f"http://www.bruckner-online.at/{record['id']}"
    record['title'] = " ".join(" ".join(doc.any_xpath('.//tei:title[@type="main"]//text()')).split())
    record['persons'] = [
         " ".join(" ".join(x.xpath('.//text()')).split()) for x in doc.any_xpath('.//tei:author')
    ]
    record['full_text'] = " ".join(''.join(body.itertext()).split())
    records.append(record)

make_index = CFTS_COLLECTION.documents.import_(records, {'action': 'upsert'})
print(make_index)
print('done with central indexing')