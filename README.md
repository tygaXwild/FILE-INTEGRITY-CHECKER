# FILE-INTEGRITY-CHECKER
A File Integrity Checker is used in real-world cybersecurity, malware detection, and forensics...

NTRODUCTION..............................................................................................................................................................................................................

File Integrity Checker

A File Integrity Checker is a host-based security tool used to verify that files on a system have not been altered without authorization. In cybersecurity, attackers often modify files to hide malicious activity or maintain persistence on a compromised system. This project implements a Python-based File Integrity Checker that helps detect such unauthorized changes by using cryptographic hashing techniques to monitor file integrity over time.

WHY DO WE NEED FILE INTEGRITY CHECKERS?...............................................................................................................................................................................................................
The need for a File Integrity Checker arises from the concept of Defense in Depth, which emphasizes the use of multiple layers of security to protect systems and data. While firewalls, authentication mechanisms, and antivirus software provide outer layers of defense, a File Integrity Checker serves as an internal monitoring mechanism. It does not prevent attacks directly, but it plays a crucial role in detecting successful intrusions by identifying unexpected file modifications. Early detection helps minimize damage and assists in incident response and system recovery.

HOW DO FILE INTEGRITY CHECKERS WORK?....................................................................................................................................................................................................................
File Integrity Checkers generally operate in two phases. In the first phase, known as the baseline creation phase, cryptographically strong hash values are generated for selected files and stored securely. These hash values act as unique digital fingerprints for each file. Any modification to the file, even a single-character change, results in a completely different hash value. This baseline serves as a trusted reference for future integrity checks.

In the second phase, the integrity verification phase, the system periodically recalculates hash values for the same files and compares them with the stored baseline. If the newly calculated hash differs from the original one, the file is flagged as modified, indicating possible tampering or unauthorized access. In cases where files are legitimately updated by authorized users, the baseline must be regenerated to avoid false alerts.

FEATURES...............................................................................................................................................................................................................
This project uses cryptographic one-way hash functions, specifically the SHA-256 algorithm, to ensure strong security and reliability. One-way hash functions generate fixed-length outputs that cannot be reversed to retrieve the original data. SHA-256 is widely used in security applications due to its resistance to collisions and its balance between performance and cryptographic strength. Weaker algorithms such as CRC-32, MD5, and SHA-1 are avoided due to known vulnerabilities.

The implemented File Integrity Checker focuses primarily on verifying file content integrity using hashing, keeping the design simple, efficient, and beginner-friendly. It provides clear alerts when file changes are detected and offers a command-line interface for ease of use. This project can be further extended to include directory monitoring, logging, real-time alerts, and additional file attribute tracking.
Overall, this File Integrity Checker demonstrates a practical and essential cybersecurity concept used in intrusion detection systems, system monitoring, and compliance solutions. It serves as an excellent foundational project for learning host-based security mechanisms and understanding how cryptographic hashing can be applied to real-world security problems.

System Requirements......................................................................................................................................................................................................

The requirements for the file integrity checker are

#Hardware

• Any modern system capable of running Python 3, Minimum 2 GB RAM (4 GB recommended),At least 100 MB free disk space,Standard display with terminal/command-line access ,Internet connection (optional, only for setup and updates)

#SOFTWARE

Operating System: Linux / macOS / Windows (32-bit or 64-bit) ,Programming Language: Python 3.8 or above and the libraries that are needed are • hashlib – for cryptographic hash generation (SHA-256)• os – for file and path handling• time – for timestamp handling (optional extension) and some other • sys/types.h • sys/mman.h • fcntl.h • openssl/md5.h • time.h

System Design...........................................................................................................................................................................................................

The File Integrity Checker is designed as a host-based monitoring tool that detects unauthorized file modifications using cryptographic hashing. The system works by creating a baseline database of file hash values and later comparing them with newly calculated hashes to identify changes.

Algorithm ...

Step 1: Start the program and display available options to the user.

Step 2: Check whether a hash file (baseline) exists for the selected file. If it does not exist, the program proceeds to create a new baseline; otherwise, it moves to integrity verification.

Step 3: Ask the user to enter the path of the file to be monitored. If the file exists, proceed; otherwise, display an error message.

Step 4: Calculate the SHA-256 hash of the selected file and store it in a separate .hash file, which acts as the initial baseline.

Step 5: Save the hash securely and notify the user that the baseline has been successfully created.

Step 6: During integrity verification, recalculate the SHA-256 hash of the same file at runtime.

Step 7: Compare the newly calculated hash with the stored baseline hash.

Step 8: If both hashes match, confirm that the file has not been modified and display a success message.

Step 9: If the hashes do not match, alert the user that the file integrity has been violated, indicating possible unauthorized modification.

Step 10: End the program.
