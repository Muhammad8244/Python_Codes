import shutil
import os

csv_file = r"C:\Users\PMLS\Downloads\annual-enterprise-survey-2023-financial-year-provisional.csv"
exe_file = r"C:\Users\PMLS\Downloads\1mb.exe"
output_file = r"C:\Users\PMLS\Downloads\combined_file2.csv"

# Combine the .exe and .csv files into one file
with open(output_file, 'wb') as wfd:
    for f in [exe_file, csv_file]:
        with open(f, 'rb') as fd:
            shutil.copyfileobj(fd, wfd)

# Determine the size of the .exe file to extract the .csv data later
exe_file_size = os.path.getsize(exe_file)

# Extract the CSV data from the combined file
with open(output_file, 'rb') as f:
    f.seek(exe_file_size)
    csv_data = f.read()

# Write the extracted CSV data to a new file
with open('extracted_file.csv', 'wb') as f:
    f.write(csv_data)
