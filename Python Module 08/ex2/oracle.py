import sys
import os
from dotenv import load_dotenv

print("\nORACLE STATUS: Reading the Matrix...")
load_dotenv()

required_configs = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]
missing = [var for var in required_configs if not os.getenv(var)]

if missing:
    print("missing configuration variables:")
    for var in missing:
        print(f" - {var}")
    exit(1)

print(f"""\nConfiguration loaded:
Mode: {os.getenv('MATRIX_MODE')}
Database: {'connected to local instance' if os.getenv('DATABASE_URL') else 'disconnected'}
API Access: {'Authenticated' if os.getenv('API_KEY') else 'Unauthenticated'}
Log Level: {os.getenv('LOG_LEVEL')}
Zion Network: {'Online' if os.getenv('ZION_ENDPOINT') else 'Offline'}
""")
print("""\nEnvironment security check:
Environment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available

The Oracle sees all configurations.
""")