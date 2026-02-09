print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
dat = None
try:
    print("Accessing Storage Vault: ancient_fragment.txt")
    dat = open("ancient_fragment.txt", "r")
    print("Connection established...\n")
    print(dat.read())
    dat.close()
except FileNotFoundError:
    print("ERROR: Storage vault not found.")
except Exception as e:
    print("Unexpected recovery error:", e)
    if dat is not None:
        dat.close()
print("\nData recovery complete. Storage unit disconnected.")
