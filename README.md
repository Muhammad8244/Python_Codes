
This is python codes repos having exiting small python scripts to do supercool things
Combining Files:
shutil.copyfileobj(fd, wfd) reads data from the .exe and .csv files and writes it to combined_file2.csv, creating a file that contains both.
Extracting Original CSV Data:
By using os.path.getsize(exe_file), it records the size of the .exe file, allowing it to "skip" over this part in the combined file.
It then seeks to this size within combined_file2.csv and reads the remaining bytes, which correspond to the CSV content.
Finally, it writes these extracted bytes to extracted_file.csv.
This project is a feature-rich, AI-assisted static malware analysis toolkit designed for malware analysts, reverse engineers, and cybersecurity researchers. It provides a graphical user interface (GUI) built with PyQt5, enabling intuitive interaction with various malware analysis capabilities. The tool is capable of parsing, analyzing, and generating reports from Windows PE (Portable Executable) files, making it ideal for use in malware labs, SOCs, and incident response environments.

🧠 Key Features:
Basic Information Extraction: Collects file name, type, size, architecture, ASLR status, timestamps, image base, and subsystem information.

Hash Calculations: Computes MD5, SHA1, SHA256, and SHA512 hashes for integrity checks and threat intelligence matching.

PE Header Analysis: Parses DOS, File, and Optional headers for anomalies and metadata.

Section Analysis: Extracts section information including entropy scores, characteristics, and suspicious indicators.

Import/Export Table Analysis: Identifies suspicious API calls often used by malware (e.g., VirtualAlloc, CreateRemoteThread, RegSetValue).

String Extraction: Extracts ASCII and Unicode strings, highlights suspicious ones (e.g., URLs, file paths, PowerShell commands).

Packer Detection: Detects common packers (e.g., UPX, Themida, VMProtect) using heuristics and entropy.

Network Activity Detection: Identifies use of networking-related APIs such as socket, connect, and HttpSendRequest.

Entry Point Disassembly: Analyzes code at the entry point and simulates basic disassembly.

Digital Signature Check: Verifies whether the binary is signed.

Anti-VM and Anti-Sandbox Detection: Detects use of API calls commonly used to evade analysis in sandbox or VM environments.

URL/IP Detection: Extracts embedded URLs and IPs from strings for threat hunting.

Payload and Code Cave Detection: Identifies NOP sleds and breakpoint instruction patterns often used by shellcode.

Suspicious Indicator Detection: Flags unusual behavior like TLS callbacks, invalid timestamps, and executable + writable sections.

Threat Scoring: Calculates a threat score (0–100) based on all extracted indicators.

Custom Rule Engine: Allows users to define new detection rules based on entropy and section names.

Timeline Generation: Maintains a step-by-step record of analysis for audit and traceability.

IOC Export: Generates CSV/JSON reports with hashes, imports, IPs, etc.

PDF Reporting: Generates professional-grade PDF reports with full analysis details.

Offline AI Classification: Uses a trained ML model to predict malware family and risk level.

Plugin Support: Supports custom Python plugins for config extraction or post-processing.

🖥️ Technologies Used:
Programming Language: Python 3

GUI Framework: PyQt5

Static Analysis Libraries: pefile, magic, hashlib, re

Machine Learning: joblib-based classifier (trained offline)

File I/O and Regex: For string extraction and pattern recognition

Threading: For asynchronous file monitoring during analysis

PDF Generation: Via QPrinter and HTML rendering

🧑‍💻 Potential Use Cases:
Malware research and reverse engineering in military or corporate environments

Static analysis in malware sandboxes and forensic labs

IOC extraction and threat hunting in SOCs

Malware triage and intelligence enrichment pipelines

