import pandas as pd
import mysql.connector
from config import MYSQL

def generate_features():
    print("Connecting to MySQL...")
    conn = mysql.connector.connect(**MYSQL)
    cursor = conn.cursor(dictionary=True)

    print("Reading data from database...")
    cursor.execute("SELECT * FROM traffic_data;")
    rows = cursor.fetchall()

    print("Converting to DataFrame...")
    df = pd.DataFrame(rows)

    # Feature engineering
    df['date_time'] = pd.to_datetime(df['date_time'])

    df['hour'] = df['date_time'].dt.hour
    df['day_of_week'] = df['date_time'].dt.dayofweek
    df['month'] = df['date_time'].dt.month

    # Peak hour classification
    df['peak_hour'] = df['hour'].apply(lambda h: 1 if (6 <= h <= 9) or (16 <= h <= 19) else 0)

    # Congestion level classification
    def congestion(vol):
        if vol < 3000:
            return "Low"
        elif vol < 6000:
            return "Moderate"
        else:
            return "High"

    df['congestion_level'] = df['traffic_volume'].apply(congestion)

    print("Prepared features DataFrame with shape:", df.shape)

    # Insert into traffic_features table
    print("Inserting engineered data into database...")
    insert_query = """
        INSERT INTO traffic_features(
            date_time, hour, day_of_week, month,
            traffic_volume, temp, rain_1h, snow_1h, clouds_all, weather_main,
            weather_description, holiday, peak_hour, congestion_level
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    conn2 = mysql.connector.connect(**MYSQL)
    cursor2 = conn2.cursor()

    rows_to_insert = []
    for _, row in df.iterrows():
        rows_to_insert.append((
            row['date_time'], row['hour'], row['day_of_week'], row['month'],
            row['traffic_volume'], row['temp'], row['rain_1h'], row['snow_1h'],
            row['clouds_all'], row['weather_main'], row['weather_description'],
            row['holiday'], row['peak_hour'], row['congestion_level']
        ))

    batch_size = 2000
    for i in range(0, len(rows_to_insert), batch_size):
        batch = rows_to_insert[i:i+batch_size]
        cursor2.executemany(insert_query, batch)
        conn2.commit()
        print(f"Inserted {i + len(batch)} rows into features table...")

    cursor2.close()
    conn2.close()
    cursor.close()
    conn.close()

    print("Feature engineering completed successfully!")

if __name__ == "__main__":
    generate_features()
