import sys
print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
id = input("Input Stream active. Enter archivist ID: ")
report = input("Input Stream active. Enter status report: ")
sys.stdout.write(f"[STANDARD] Archive status from {id}: {report}\n")
sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
sys.stdout.write("[STANDARD] Data transmission complete\n")
print("Three-channel communication test successful.")