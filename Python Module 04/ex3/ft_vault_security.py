print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
print("Initiating secure vault access..."
      "Vault connection established with failsafe protocols")
print("SECURE EXTRACTION:")
with open("classified_data.txt", "r") as vault:
    print(vault.read())

with open("classified_data.txt", "a") as log:
    print("SECURE PRESERVATION:")
    log.write("\n[CLASSIFIED] New security protocols archived\n")
    print("[CLASSIFIED] New security protocols archived")
print("Vault automatically sealed upon completion")

print("All vault operations completed with maximum security.")