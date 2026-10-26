# Network Traffic Analyzer

import csv

with open("sample_traffic.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Source IP:", row["Source"])
        print("Destination IP:", row["Destination"])
        print("Protocol:", row["Protocol"])
        print("Packet length:", row["Length"])
        break
