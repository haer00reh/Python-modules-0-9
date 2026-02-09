print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
try:
    print("Initializing new storage unit: new_discovery.txt")
    dat = open("new_discovery.txt", "w")
    print("Storage unit created successfully...")
    dat.write("[ENTRY 001] New quantum algorithm discovered\n"
              "[ENTRY 002] Efficiency increased by 347%\n"
              "[ENTRY 003] Archived by Data Archivist trainee\n")
    dat.close()
    print("\nInscribing preservation data...")
    dat = open("new_discovery.txt", "r")
    content = dat.read()
    print(content)
    dat.close()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
except Exception as e:
    print(f"ERROR: {e}")
