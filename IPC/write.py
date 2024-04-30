# write.py
import sys

try:
    with open("data.txt", "w") as writer:
        while True:
            input_data = input()
            if input_data.strip() == "":
                break
            writer.write(input_data + "\n")
            writer.flush()
except IOError as e:
    print("Error:", e)
