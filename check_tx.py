import psycopg2

try:
    # Connect to your Proxmox Container
    connection = psycopg2.connect(
        user="postgres",
        password="wallester_test",
        host="192.168.8.101", # Your Container IP
        port="5432",
        database="wallester_lab"
    )

    cursor = connection.cursor()
    
    # The "Support Ticket" Query
    cursor.execute("SELECT * FROM transactions WHERE status = 'failed';")
    failed_tx = cursor.fetchall()

    print(f"--- ALERT: Found {len(failed_tx)} Failed Transactions ---")
    for tx in failed_tx:
        print(f"ID: {tx[0]} | User: {tx[1]} | Amount: {tx[2]} {tx[3]} | Merchant: {tx[5]}")

except Exception as error:
    print(f"Error connecting to Proxmox DB: {error}")

finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()
