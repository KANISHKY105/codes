## Invalid Token based algorithm code ##

from collections import deque

class Site:
    def __init__(self, site_id, num_sites):
        self.site_id = site_id
        self.RN = [0] * num_sites
        self.LN = [0] * num_sites

class SuzukiKasami:
    def __init__(self, num_sites, initial_token_site_id):
        self.num_sites = num_sites
        self.sites = [Site(i + 1, num_sites) for i in range(num_sites)]
        self.current_token_holder = initial_token_site_id
        self.token_queue = deque()

    def simulate(self):
        while True:
            print("Site", self.current_token_holder, "has the token.")
            print("Site", self.current_token_holder, "executes critical section.")
            current_site = self.sites[self.current_token_holder - 1]
            current_site.LN[self.current_token_holder - 1] = current_site.RN[self.current_token_holder - 1]
            for j in range(self.num_sites):
                if j + 1 not in self.token_queue and current_site.RN[j] == current_site.LN[j] + 1:
                    self.token_queue.append(j + 1)
            if self.token_queue:
                next_token_holder = self.token_queue.popleft()
                print("Token sent from Site", self.current_token_holder, "to Site", next_token_holder)
                self.current_token_holder = next_token_holder
            else:
                print("Site", self.current_token_holder, "retains the token.")
            requesting_site_id = int(input("Enter the site ID that wants to enter the critical section (1-" + str(self.num_sites) + "): "))
            if requesting_site_id < 1 or requesting_site_id > self.num_sites:
                print("Invalid site ID.")
                return
            self.request_critical_section(requesting_site_id)

    def request_critical_section(self, requesting_site_id):
        print("Site", requesting_site_id, "requests the critical section.")
        current_site = self.sites[requesting_site_id - 1]
        current_site.RN[requesting_site_id - 1] += 1
        for i in range(self.num_sites):
            if i != requesting_site_id - 1:
                current_site.RN[i] = max(current_site.RN[i], self.sites[i].RN[requesting_site_id - 1])
                if self.current_token_holder == i + 1 and current_site.RN[i] == current_site.LN[i] + 1:
                    self.token_queue.append(requesting_site_id)
                    break  # Exit loop after finding the next token holder

if __name__ == "__main__":
    num_sites = int(input("Enter the number of sites: "))
    initial_token_site_id = int(input("Enter the site ID which initially has the token (1-" + str(num_sites) + "): "))
    if initial_token_site_id < 1 or initial_token_site_id > num_sites:
        print("Invalid site ID for initial token holder.")
    else:
        suzuki_kasami = SuzukiKasami(num_sites, initial_token_site_id)
        suzuki_kasami.simulate()
























