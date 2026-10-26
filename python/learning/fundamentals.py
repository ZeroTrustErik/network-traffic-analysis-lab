# Python Fundamentals
#

print("Network Traffic Analyzer")
print("Python environment is working!")

source_ip = "192.168.12.181"
destination_ip = "1.1.1.1"
protocol = "ICMP"
packet_length = 74
response_time = 506.203
packet_count = 8
packet_count += 5
average_packet_size = packet_length / 2
capture_tool = "Wireshark"

print(source_ip)
print(protocol)
print(packet_length)
print(packet_count)
print(capture_tool)
print(type(packet_count))
print(average_packet_size)
print(type(response_time))

protocols = ["DNS", "ICMP", "DNS", "TCP", "ICMP"]
print(protocols[0])
print(protocols[3])

for protocol in protocols:
    print(protocol)

print(len(protocols))
print(protocols[-1])

for protocol in protocols:
    if protocol == "DNS":
        print("DNS packet detected")
    elif protocol == "ICMP":
        print("ICMP packet detected")
    else:
        print("Other protocol detected")

dns_count = 0
icmp_count = 0
other_count = 0

for protocol in protocols:
    if protocol == "DNS":
        dns_count += 1
    elif protocol == "ICMP":
        icmp_count += 1
    else:
        other_count += 1

print("DNS packets:", dns_count)
print("ICMP packets:", icmp_count)
print("Other packets:", other_count)