from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Create an RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server listening on port 8000...")

# Register functions
server.register_function(add, "add")
server.register_function(subtract, "subtract")

# Run the server
server.serve_forever()
