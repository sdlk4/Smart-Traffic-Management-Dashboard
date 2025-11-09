import pandas as pd
import mysql.connector
from config import MYSQL
from datetime import datetime

# Path to your CSV file
CSV_PATH ="C:\\Users\\srika\\OneDrive\\Desktop\\smart_traffic\\data\\raw\\Metro_Interstate_Traffic_Volume.csv"


def clean_datetime(dt):
    # Convert to Python datetime object safely
    try:
        return pd.to_datetime(dt)
    except:
        return None

def load_csv():
    print("Loading CSV...")
    df = pd.read_csv(CSV_PATH)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Force string first to avoid weird dtype issues
    df['date_time'] = df['date_time'].astype(str)

    # Parse date_time safely
    df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce')

    # Debug check for null timestamps
    null_count = df['date_time'].isnull().sum()
    print(f"Null date_time values found: {null_count}")

    # Drop null date_time rows
    df = df.dropna(subset=['date_time'])

    # CLEAN holiday column (this is the line you asked about)
    df['holiday'] = df['holiday'].astype(str).str.strip()

    # Replace NaN with None for MySQL
    df = df.where(pd.notnull(df), None)

    print("CSV loaded. Total rows after cleaning:", len(df))
    return df




def insert_into_mysql(df):
    print("Connecting to MySQL...")
    conn = mysql.connector.connect(**MYSQL)
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO traffic_data (
            date_time, traffic_volume, temp, rain_1h, snow_1h, clouds_all,
            weather_main, weather_description, holiday
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    print("Inserting rows into database...")

    #  Reorder columns to match SQL insert order exactly
    df = df[['date_time', 'traffic_volume', 'temp', 'rain_1h', 'snow_1h',
             'clouds_all', 'weather_main', 'weather_description', 'holiday']]

    # Convert NaN/None correctly
    df = df.where(pd.notnull(df), None)

    rows = list(df.itertuples(index=False, name=None))

    batch_size = 1000
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i + batch_size]
        cursor.executemany(insert_query, batch)
        conn.commit()
        print(f"Inserted {i + len(batch)} rows...")

    cursor.close()
    conn.close()
    print("All rows inserted successfully!")


def main():
    df = load_csv()
    insert_into_mysql(df)

if __name__ == "__main__":
    main()
