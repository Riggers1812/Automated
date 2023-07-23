import os
from pathlib import Path

my_folder = Path(r"C:\Users\dtrig\Downloads\Documents\Pdfs")

my_files = os.listdir(my_folder)

wages = []

for file in my_files:
    if path.stem.("DRigby_ONPAYEMAIL_*") == file:
        wages.append(file)

destination = Path(r"E:\Users\dtrig\Documents\Work\JD PLC\Wages")

for wage_packet in wages:
    new_path = [destination + "\\" + wage_packet]
    # pathlib.Path(wage_packet.rename(destination))

print(new_path)
