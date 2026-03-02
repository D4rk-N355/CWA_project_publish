def prepare_row_for_sql(cleaned_dict):
    return (
        cleaned_dict.get('station_id'),
        cleaned_dict.get('obs_time'),
        cleaned_dict.get('airtemperature'), 
        cleaned_dict.get('relativehumidity'),
        cleaned_dict.get('airpressure'),
        cleaned_dict.get('rain'),
        cleaned_dict.get('windspeed'),
        cleaned_dict.get('day_high'),
        cleaned_dict.get('day_low')
    )

import sqlite3

def loadpulse_batch_save(db_path, cleaned_dicts):
    """
    將多個清洗後的字典轉換為 Tuple List,並一次性寫入 SQL。
    """
    rows_to_insert = [prepare_row_for_sql(d) for d in cleaned_dicts if d.get('station_id')]

    if not rows_to_insert:
        print("⚠️ 沒有可寫入的資料。")
        return

    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        sql = """
            INSERT OR IGNORE INTO Weather_Logs 
            (station_id, obs_time, temp, humid, pressure, rain, wind_speed, day_high, day_low)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        cursor.executemany(sql, rows_to_insert)
        
     
        conn.commit()
        print(f"✅ 成功處理 {len(rows_to_insert)} 筆觀測紀錄並寫入資料庫。")
        
    except Exception as e:
        print(f"❌ 寫入資料庫時發生錯誤: {e}")
        conn.rollback() # 如果失敗就撤回，保持資料庫乾淨
    finally:
        conn.close()