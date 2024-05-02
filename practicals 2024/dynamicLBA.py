class LeastConnectionLoadBalancer:
    def __init__(self):
        self.server_connections = {}

    def add_server(self, server_name, initial_connections=0):
        # Add a server to the load balancer with specified initial connections
        self.server_connections[server_name] = initial_connections

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

    # Add servers to the load balancer with initial connections
    load_balancer.add_server("Server1")
    load_balancer.add_server("Server2")
    load_balancer.add_server("Server3")
    load_balancer.add_server("Server4", initial_connections=2)  # Add Server4 with 2 initial connections

    # Simulate requests and print the server to which each request is routed
    for i in range(15):
        selected_server = load_balancer.get_server_with_least_connections()
        print(f"Request {i + 1}: Routed to {selected_server}")
