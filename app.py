import re
import csv
from collections import defaultdict

# threshhold for suspecious activity
THRESHOLD = 5

def parse_log_file(file_path):
    ip_requests = defaultdict(int)
    endpoint_access = defaultdict(int)
    failed_logins = defaultdict(int)

    with open(file_path, 'r') as log_file:
        for line in log_file:

            # get ip address
            ip_match = re.match(r'(\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip_address = ip_match.group(1)
                ip_requests[ip_address] += 1

            # get endpoint and status code
            endpoint_match = re.search(r'\"\w+ (\S+) HTTP/\d\.\d\" (\d+)', line)
            if endpoint_match:
                endpoint = endpoint_match.group(1)
                status_code = int(endpoint_match.group(2))
                endpoint_access[endpoint] += 1

                # find failed login attempts
                if status_code == 401 or "Invalid credentials" in line:
                    failed_logins[ip_address] += 1
                    
    return ip_requests, endpoint_access, failed_logins

def count_requests(ip_requests):
    # print(len(ip_requests))
    sorted_requests = sorted(ip_requests.items(), key=lambda x: x[1], reverse=True)
    print("\nIP Address \t Request Count")
    for ip, count in sorted_requests:
        print(f"{ip:<20}{count}")
    return sorted_requests

def most_accessed(endpoint_access):
    # print(len(endpoint_access))
    most_accessed = max(endpoint_access.items(), key=lambda x: x[1])
    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")
    return most_accessed

def detect_suspicious_activity(failed_logins):
    # print(len(failed_logins))
    suspicious_ips = {ip: count for ip, count in failed_logins.items() if count >= THRESHOLD}
    print("\nSuspicious Activity Detected:")
    print("IP Address \t Failed Login Attempts")
    for ip, count in suspicious_ips.items():
        print(f"{ip:<20}{count}")
# no failed logins
    if not suspicious_ips:
        print("\nNo suspicious activity detected.")

    return suspicious_ips

def save_results_to_csv(ip_requests, most_accessed, suspicious_ips):
    with open('log_analysis_results.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write Requests per IP
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in ip_requests:
            writer.writerow([ip, count])

        # Most Accessed Endpoint
        writer.writerow([])
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerow([most_accessed[0], most_accessed[1]])

        # Suspicious Activity
        writer.writerow([])  # Blank row
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in suspicious_ips.items():
            writer.writerow([ip, count])

def main():
    log_file_path = 'sample.log'
    ip_requests, endpoint_access, failed_logins = parse_log_file(log_file_path)

# per ip request count
    sorted_requests = count_requests(ip_requests)

# most frequently used endpoints
    most_access = most_accessed(endpoint_access)

# failed logins
    suspicious_ips = detect_suspicious_activity(failed_logins)

# Save results to CSV
    save_results_to_csv(sorted_requests, most_access, suspicious_ips)

if __name__ == "__main__":
    main()
