import re

def parse_trace(trace_file):
    with open(trace_file, 'r') as file:
        lines = file.readlines()

    icmp_responses = {}
    sent_packets = []

    for line in lines:
        if 'ttl' in line and 'proto TCP' in line:
            sent_packets.append(line)
        elif 'proto ICMP' in line and 'time exceeded' in line:
            match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ip_address = match.group(1)
                timestamp = float(line.split()[0])
                icmp_responses[ip_address] = timestamp

    return sent_packets, icmp_responses

def calculate_rtt(sent_packets, icmp_responses):
    results = []
    for packet in sent_packets:
        ttl_match = re.search(r'ttl (\d+)', packet)
        id_match = re.search(r'id (\d+)', packet)
        if ttl_match and id_match:
            ttl = int(ttl_match.group(1))
            packet_id = id_match.group(1)
            sent_time = float(packet.split()[0])

            for ip, recv_time in icmp_responses.items():
                if packet_id in packet:
                    rtt = (recv_time - sent_time) * 1000
                    results.append((ttl, ip, rtt))

    return results

def main():
    trace_file = 'trace.txt'
    sent_packets, icmp_responses = parse_trace(trace_file)
    results = calculate_rtt(sent_packets, icmp_responses)

    for ttl, ip, rtt in results:
        print(f'TTL {ttl} {ip} {rtt:.2f} ms')

if __name__ == '__main__':
    main()
