import os

# Base URL for GitHub raw content
base_url = "https://raw.githubusercontent.com/zero-given/test_IMG/master/3d_frames_X"
directory = "3d_frames_X"

# Get all PNG files in the directory
png_files = sorted([f for f in os.listdir(directory) if f.endswith('.png')])

# Generate URLs and write to OUTPUT.md
with open('OUTPUT.md', 'w') as f:
    for png_file in png_files:
        url = f"{base_url}/{png_file}"
        f.write(f"{url}\n")
