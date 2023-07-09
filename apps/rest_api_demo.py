import requests
import json

# The URL to your MaxScale REST API
maxscale_url = "http://127.0.0.1:8989/v1/"

# The authentication details
auth = ("admin", "your_password")

# The SQL query you want to execute
query = "SHOW GRANTS FOR 'admin'@'localhost';"

# The database you want to query
database = "production"

# Create the payload
payload = {"jsonrpc": "2.0", "id": 42, "method": "execute_sql", "params": {"stmt": query, "database": database}}

# Execute the request
response = requests.post(maxscale_url + "sql", auth=auth, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

# Print the returned data
print(json.dumps(response.json(), indent=4))
