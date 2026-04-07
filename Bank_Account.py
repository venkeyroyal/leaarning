import sys

# Replace input() with command-line argument
if len(sys.argv) > 1:
    name = sys.argv[1]  # Jenkins passes ACCOUNT_NAME
else:
    name = "DefaultName"  # fallback if no argument given

print(f"Account name: {name}")
