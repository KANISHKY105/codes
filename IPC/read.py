# read.py
try:
    with open("data.txt", "r") as reader:
        for line in reader:
            print("Received:", line.strip())
except IOError as e:
    print("Error:", e)
