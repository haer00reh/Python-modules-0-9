import sys
try:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    id = input("Input Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")
    print(f"[STANDARD] Archive status from {id}: {report}\n")
    print("[ALERT] System diagnostic: "
          "Communication channels verified\n", file=sys.stderr)
    print("[STANDARD] Data transmission complete\n")
    print("Three-channel communication test successful.")
except Exception as e:
    print(f"ERROR: Communication failure - {e}", file=sys.stderr)
