import psycopg2
import random
from datetime import datetime
# --- CONFIGURATION ---
DB_CONFIG = {
    "host": "192.168.8.101",
    "database": "wallester_lab",
    "user": "postgres",
    "password": "wallester_test", # The one we set earlier
    "port": "5432"
}

# Real-world fintech data mocks
MERCHANTS = ["Amazon", "Netflix", "Rimi", "Tallink", "Wolt", "Bolt", "Apple Store", "Selver"]
STATUSES = ["completed", "completed", "completed", "failed", "pending"] # Weighted towards success

def generate_fake_data(count):
    data = []
    for _ in range(count):
        user_id = random.randint(100, 500)
        amount = round(random.uniform(1.00, 500.00), 2)
        merchant = random.choice(MERCHANTS)
        status = random.choice(STATUSES)
        data.append((user_id, amount, status, merchant))
    return data

try:
    print("Connecting to Proxmox Database...")
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    print(f"Generating 1000 fake transactions...")
    transactions = generate_fake_data(50000)

    # The SRE way: execute_batch is much faster than a loop
    from psycopg2.extras import execute_batch
    query = "INSERT INTO transactions (user_id, amount, status, merchant_name) VALUES (%s, %s, %s, %s)"
    
    execute_batch(cur, query, transactions)
    conn.commit()

    print("✅ Success! 1000 rows injected into 'wallester_lab'.")

except Exception as e:
    print(f"❌ Error: {e}")
finally:
    if 'conn' in locals():
        cur.close()
        conn.close()
