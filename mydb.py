import mysql.connector

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    port=3306  # Specify the port if it's not the default 3306
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Execute the CREATE DATABASE query
cursorObject.execute("CREATE DATABASE IF NOT EXISTS testDB")

# Commit the changes
dataBase.commit()

# Close the cursor and connection
cursorObject.close()
dataBase.close()

print("All Done!")