print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
try:
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as crisis_file:
            print("SUCCESS: Archive located")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    try:
        print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", "r") as vault_file:
            print("SUCCESS: vault accessed")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    with open("standard_archive.txt", "r") as standard_file:
        print(f"SUCCESS: Archive recovered - `{standard_file.read()}`")
except Exception as e:
    print(f"RESPONSE: {e}")
print("STATUS: Normal operations resumed")
print("\nAll crisis scenarios handled successfully. Archives secure.")
