# Python_Codes
This is python codes repos having exiting small python scripts to do supercool things
Combining Files:
shutil.copyfileobj(fd, wfd) reads data from the .exe and .csv files and writes it to combined_file2.csv, creating a file that contains both.
Extracting Original CSV Data:
By using os.path.getsize(exe_file), it records the size of the .exe file, allowing it to "skip" over this part in the combined file.
It then seeks to this size within combined_file2.csv and reads the remaining bytes, which correspond to the CSV content.
Finally, it writes these extracted bytes to extracted_file.csv.
