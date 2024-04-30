## Dynamic Load Balancer ##
# Least Connection Method Load Balancing Algorithm #
class LeastConnectionLoadBalancer:
    def __init__(self):
        self.server_connections = {}

    def add_server(self, server_name):
        # Add a server to the load balancer with 0 initial connections
        self.server_connections[server_name] = 0

    def get_server_with_least_connections(self):
        # Find the server with the least active connections
        min_connections = float('inf')
        selected_server = None

        for server, connections in self.server_connections.items():
            if connections < min_connections:
                min_connections = connections
                selected_server = server

        # Increment the connection count for the selected server
        if selected_server is not None:
            self.server_connections[selected_server] += 1

        return selected_server

if __name__ == "__main__":
    # Create a Least Connection load balancer
    load_balancer = LeastConnectionLoadBalancer()

    # Add servers to the load balancer
    load_balancer.add_server("Server1")
    load_balancer.add_server("Server2")
    load_balancer.add_server("Server3")

    # Simulate requests and print the server to which each request is routed
    for i in range(10):
        selected_server = load_balancer.get_server_with_least_connections()
        print(f"Request {i + 1}: Routed to {selected_server}")




































'''
Of course! Let's break down the logic of the code:

LeastConnectionLoadBalancer class:
The LeastConnectionLoadBalancer class is defined to manage the connections for each server and provide a method to get the server with the least active connections.
In the constructor (__init__ in Python), it initializes an empty dictionary named server_connections to keep track of the number of connections for each server.
add_server() method:
This method adds a server to the load balancer with an initial connection count of 0.
It takes the server_name as input and adds an entry to the server_connections dictionary with the server name as the key and 0 as the initial connection count.
get_server_with_least_connections() method:
This method finds the server with the least active connections.
It initializes min_connections to positive infinity and selected_server to None.
It iterates through each server in the server_connections dictionary and compares the number of connections for each server.
If a server has fewer connections than the current minimum, it updates min_connections and selected_server.
After iterating through all servers, it increments the connection count for the selected server by 1.
Finally, it returns the name of the selected server.
Main part of the code (within if __name__ == "__main__":):
Creates an instance of the LeastConnectionLoadBalancer class.
Adds servers to the load balancer using the add_server() method.
Simulates 10 requests to the load balancer by repeatedly calling the get_server_with_least_connections() method.
For each request, it prints the request number along with the server that the request is routed to.
The Least Connection Method Load Balancing Algorithm ensures that incoming requests are routed to the server with the least number of active connections, thus distributing the load evenly across the servers
'''