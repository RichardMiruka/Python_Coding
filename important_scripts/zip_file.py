# creating a zip file using python

import zipfile

files = ['file1.txt', 'file2.txt', 'file3.txt']

with zipfile.ZipFile('pycl.zip', 'w') as zipf:
    for file in files:
        zipf.write(file)

print("Zip file created successfully.")
