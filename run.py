
from service.config import RAW_DATA_DIR
from service.config import DATABASE_PATH
from service.init_fetch import loadpulse_init_fetch
from service.data_washing import loadpulse_universal_cleaner
from service.data_streaming import loadpulse_batch_save
import json
import time
import gzip
from dotenv import load_dotenv
import os

discord_url = os.getenv("DISCORD_URL")
raw_json = loadpulse_init_fetch()

filename = f"{RAW_DATA_DIR}/{int(time.time())}.json.gz"
with gzip.open(filename, "wt", encoding="utf-8") as f:
    json.dump(raw_json, f, ensure_ascii=False, separators=(",", ":"))

stations_list = raw_json.get('records', {}).get('Station', [])
batch_cleaned_rows = []
for station_node in stations_list:
    single_cleaned_dict = loadpulse_universal_cleaner(station_node)
    if single_cleaned_dict.get('station_id'):
        batch_cleaned_rows.append(single_cleaned_dict)

if batch_cleaned_rows:
    print(f"✅ 成功清洗 {len(batch_cleaned_rows)} 站資料")
    print(f"第一站範例：{batch_cleaned_rows[0]}")

loadpulse_batch_save(DATABASE_PATH,batch_cleaned_rows)



