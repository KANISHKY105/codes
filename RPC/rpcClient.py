import xmlrpc.client

# Connect to the RPC server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call remote functions
result_add = proxy.add(5, 3)
result_subtract = proxy.subtract(10, 4)

print("Result of add:", result_add)
print("Result of subtract:", result_subtract)
