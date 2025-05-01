import pandas as pd
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='thanigai@1234',
    database='food_waste_db'
)
cursor = conn.cursor()

# Load Providers
providers = pd.read_csv('D:/Project/Guvi_Project/local_food_waste_system/data/providers_data.csv')
for _, row in providers.iterrows():
    cursor.execute("""
        INSERT INTO providers VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))
print(providers.head())
# Load Receivers
receivers = pd.read_csv('D:/Project/Guvi_Project/local_food_waste_system/data/receivers_data.csv')
for _, row in receivers.iterrows():
    cursor.execute("""
        INSERT INTO receivers VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))
print(receivers.head())
# Load Food Listings
food = pd.read_csv('D:/Project/Guvi_Project/local_food_waste_system/data/food_listings_data.csv')
food['Expiry_Date'] = pd.to_datetime(food['Expiry_Date']).dt.date
for _, row in food.iterrows():
    cursor.execute("""
        INSERT INTO food_listings VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))
print(food.head())
# Load Claims
claims = pd.read_csv('D:/Project/Guvi_Project/local_food_waste_system/data/claims_data.csv')
claims['Timestamp'] = pd.to_datetime(claims['Timestamp'])
for _, row in claims.iterrows():
    cursor.execute("""
        INSERT INTO claims VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))
print(claims.head())
conn.commit()
conn.close()
