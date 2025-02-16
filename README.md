# Log Analysis Tool 🛠️📊

This **Log Analysis Tool** is a Python-based script designed to parse web server logs, analyze activity, and detect suspicious behavior. The script provides insights into the number of requests per IP address, the most frequently accessed endpoint, and failed login attempts, while also saving the results to a CSV file for further analysis.

---

## Features 🚀

- **Request Analysis:** Count the number of requests made by each IP address.
- **Endpoint Insights:** Identify the most frequently accessed endpoints.
- **Suspicious Activity Detection:** Detect IP addresses with failed login attempts exceeding a configurable threshold.
- **CSV Export:** Save analyzed results, including requests, endpoint data, and suspicious activity, to a CSV file.

---

## Prerequisites 📋

Ensure you have the following installed:
- Python 3.6+
- Required libraries: `re`, `csv`, `collections` (Standard Python Libraries)

---

## How It Works 🛠️

1. **Parse Log File:** 
   - Extract IP addresses, endpoints, status codes, and failed login attempts from a log file.
2. **Analyze Data:**
   - Count requests per IP address.
   - Identify the most frequently accessed endpoint.
   - Detect IPs with failed login attempts exceeding the defined threshold (default: 5).
3. **Save Results:** 
   - Export the analyzed data to a CSV file (`log_analysis_results.csv`).

---

## Installation 🔧

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/VRV-assignment.git
   ```
2. Navigate to the project directory:
   ```bash
   cd VRV-assignment
   ```

---

## Usage ✨

1. Place your log file in the project directory. Make sure it's named `sample.log` or adjust the file path in the `main()` function.
2. Run the script:
   ```bash
   python app.py
   ```
3. View the results directly in the console and in the `log_analysis_results.csv` file generated in the project directory.

---

## Configuration ⚙️

To change the suspicious activity threshold, modify the `THRESHOLD` variable at the top of the script:
```python
THRESHOLD = 10  # Set your desired threshold for failed login attempts
```

---

## Output 📊

### Console Output:
- **Requests per IP:** A list of IPs with the corresponding number of requests.
- **Most Accessed Endpoint:** The endpoint accessed most frequently.
- **Suspicious Activity:** IPs with failed login attempts exceeding the threshold.

### CSV File:
The `log_analysis_results.csv` file contains:
- Requests per IP.
- Most accessed endpoint and its access count.
- Suspicious IPs and the count of their failed login attempts.

---

## Example Log File Format 📁

Ensure your log file (`sample.log`) contains lines in a format similar to:
```
192.168.1.1 - - [15/Feb/2025:14:32:00 +0000] "GET /index.html HTTP/1.1" 200 -
192.168.1.2 - - [15/Feb/2025:14:32:10 +0000] "POST /login HTTP/1.1" 401 - "Invalid credentials"
```

---

## Example CSV Output 📂

Sample `log_analysis_results.csv`:
```
Requests per IP
IP Address,Request Count
192.168.1.1,10
192.168.1.2,7

Most Accessed Endpoint
Endpoint,Access Count
/index.html,15

Suspicious Activity
IP Address,Failed Login Count
192.168.1.2,6
```

---

## Contribution Guidelines 🤝

We welcome contributions to enhance this tool! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to the branch:
   ```bash
   git commit -m "Add feature description"
   git push origin feature-name
   ```
4. Open a Pull Request.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments 🙏

- **Regex for Log Parsing:** Inspired by common log parsing techniques.
- **CSV Handling:** Built using Python's `csv` module.

---

**Happy Analyzing!** 🛠️
