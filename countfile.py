import csv
import os
from collections import defaultdict

folder_path = "downloads"
id_counts = defaultdict(int)

for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        with open(os.path.join(folder_path, filename)) as f:
            reader = csv.reader(f)
            header = next(reader) # skip header row
            for row in reader:
                id = row[1] # assuming id is the first column in the csv file
                id_counts[id] += 1

# with open("downloads/20230104_user_photo.csv") as f:
#     reader = csv.reader(f)
#     header = next(reader) # skip header row
#     for row in reader:
#         id = row[1] # assuming id is the first column in the csv file
#         id_counts[id] += 1

print(id_counts)
# Write the results to a new CSV file
with open("Coordination_ID_022023.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["coordination_id", "count"])
    for id, count in id_counts.items():
        writer.writerow([id, count])