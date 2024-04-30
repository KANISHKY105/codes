## Static Load Balancer ##
#Round Robin#
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_next_server(self):
        next_server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return next_server

if __name__ == "__main__":
    # Sample list of servers
    server_list = ["Server1", "Server2", "Server3"]

    # Create a load balancer with the server list
    load_balancer = LoadBalancer(server_list)

    # Simulate requests to the load balancer
    for i in range(10):
        next_server = load_balancer.get_next_server()
        print(f"Request {i + 1}: Routed to {next_server}")



































'''
Certainly! Let's break down the logic of the code:

LoadBalancer class:
The LoadBalancer class is defined to manage a list of servers and provide a method to get the next server in a round-robin manner.
In the constructor (__init__ in Python), it initializes the servers list and sets the current_index to 0.
get_next_server() method:
This method returns the next server in the list based on the current index.
It retrieves the server at the current index from the servers list.
It then increments the current_index by 1 and takes the modulo operation with the length of the servers list to ensure it wraps around when reaching the end of the list.
Finally, it returns the next server.
Main part of the code (within if __name__ == "__main__":):
Defines a sample list of servers named server_list.
Creates an instance of the LoadBalancer class with the server_list.
Simulates 10 requests to the load balancer by repeatedly calling the get_next_server() method.
For each request, it prints the request number along with the server that the request is routed to.
The round-robin algorithm ensures that each server in the list gets an equal share of requests by rotating through the list of servers sequentially. This helps distribute the load evenly across the servers.
'''