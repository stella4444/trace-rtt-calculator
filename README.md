# trace_rtt_calculator
This script analyzes network trace files to calculate Round-Trip Time (RTT) of packets. It processes trace data to identify sent packets and their corresponding ICMP responses, computes RTT values, and displays the results.

## Overview
The script consists of three main functions:
1. **parse_trace(trace_file)**: Parses the trace file to extract sent packets and ICMP responses.
2. **calculate_rtt(sent_packets, icmp_responses)**: Calculates RTT for each sent packet based on ICMP responses.
3. **main()**: Orchestrates the parsing and RTT calculation processes, and outputs the results.

## Usage
1. Place your trace file in the same directory as the script or specify the full path in the trace_file variable within the main() function.
2. Run the script using Python:
**python trace_rtt_analyzer.py**
3. View the output which displays TTL, IP addresses, and RTT values.

# Example Output
TTL 64 192.168.1.1 25.78 ms
TTL 128 10.0.0.1 30.12 ms

# Requirements
Python 3.x

# Notes
Ensure the trace file format matches the expected structure for proper parsing.
The script assumes that each packet's unique ID can be found in both sent packets and ICMP responses to match RTT calculations accurately.

## Function
**parse_trace(trace_file)**
Parameters: 
+ trace_file (str): The path to the trace file to be processed.
Returns: 
+ sent_packets (list): A list of lines from the trace file where packets are sent.
+ icmp_responses (dict): A dictionary where keys are IP addresses and values are timestamps of ICMP responses.
Description: Reads the trace file, identifies lines indicating sent packets and ICMP responses, and extracts relevant information including IP addresses and timestamps.

**calculate_rtt(sent_packets, icmp_responses)**
Parameters:
+ sent_packets (list): A list of lines representing sent packets.
+ icmp_responses (dict): A dictionary of ICMP response timestamps keyed by IP address.
Returns:
+ results (list): A list of tuples containing TTL, IP address, and RTT in milliseconds.
Description: Calculates the RTT for each packet by comparing its sent time with the time of its corresponding ICMP response. RTT is computed in milliseconds.

**main()**
Description:
+ Defines the path to the trace file.
+ Calls parse_trace() to get sent packets and ICMP responses.
+ Calls calculate_rtt() to compute RTT values.
+ Prints the results in a human-readable format showing TTL, IP address, and RTT.

