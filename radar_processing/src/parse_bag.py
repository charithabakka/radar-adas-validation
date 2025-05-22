from bagpy import bagreader
import os
import shutil

bag_path = r"C:\Users\chari\Desktop\radar-adas-validation\radar_processing\data\raw\ars548\2023-07-05-10-34-03.bag"
output_folder = r"C:\Users\chari\Desktop\radar-adas-validation\radar_processing\data\processed"

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

bag = bagreader(bag_path)

print("Available topics:")
print(bag.topics)

for topic in bag.topics:
    print(f"Exporting topic: {topic}")
    csv_path = bag.message_by_topic(topic)

    # Move the exported CSV to your processed folder
    filename = os.path.basename(csv_path)
    new_path = os.path.join(output_folder, filename)
    shutil.move(csv_path, new_path)

    print(f"✅ Exported {topic} to {new_path}")

print("\nAll topics exported and moved!")


