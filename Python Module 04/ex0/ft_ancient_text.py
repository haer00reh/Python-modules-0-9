print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
try:
    print("Accessing Storage Vault: ancient_fragment.txt")
    dat = open("ancient_fragment.txt", "r")
    print("Connection established...\n")
    print(dat.read())
    dat.close()
except FileNotFoundError:
    print("ERROR: Storage vault not found.")
print("\nData recovery complete. Storage unit disconnected.")
