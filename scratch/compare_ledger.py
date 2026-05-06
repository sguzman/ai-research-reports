import os
import re

ledger_path = 'data/docx-md-crosswalk.toml'
docx_dir = 'data/docx'

ledger_files = set()
with open(ledger_path, 'r') as f:
    for line in f:
        match = re.search(r'file = "(.*)"', line)
        if match:
            ledger_files.add(match.group(1))

actual_files = set(os.listdir(docx_dir))

missing_in_ledger = actual_files - ledger_files
missing_on_disk = ledger_files - actual_files

# Some files might have different quotes or escaping in the TOML
# but for a quick check this should be fine.

print(f"Files in docx/ but NOT in ledger: {len(missing_in_ledger)}")
for f in sorted(missing_in_ledger):
    print(f"  - {f}")

print(f"\nFiles in ledger but NOT on disk: {len(missing_on_disk)}")
for f in sorted(missing_on_disk):
    print(f"  - {f}")
