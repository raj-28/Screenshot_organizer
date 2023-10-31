import os
import shutil
import re
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description="Organize screenshots on your Desktop.")
    parser.add_argument("--source", default=os.path.expanduser("~/Desktop"), help="Source directory (default: Desktop)")
    parser.add_argument("--destination", default=os.path.expanduser("~/Documents/Screenshots"), help="Destination directory (default: Documents/Screenshots)")
    args = parser.parse_args()

    # Define the source and destination directories
    desktop_path = args.source
    screenshots_path = args.destination

    # Create the Screenshots folder if it doesn't exist
    if not os.path.exists(screenshots_path):
        os.mkdir(screenshots_path)

    # List files on the Desktop
    desktop_files = os.listdir(desktop_path)

    # Define a regular expression pattern to match screenshot files
    screenshot_pattern = r'Screen Shot.*\.png'

    for file_name in desktop_files:
        if re.match(screenshot_pattern, file_name):
            # Build the full path of the screenshot on the Desktop
            src_path = os.path.join(desktop_path, file_name)

            # Build the full path for the destination
            dest_path = os.path.join(screenshots_path, file_name)

            # Check if the file already exists in the Screenshots folder
            if not os.path.exists(dest_path):
                # Move the file to the Screenshots folder
                shutil.move(src_path, dest_path)
                print(f"Moved '{file_name}' to {screenshots_path}")
            else:
                # Generate a unique filename by adding a timestamp
                timestamp = time.strftime("%Y%m%d%H%M%S")
                dest_path = os.path.join(screenshots_path, f"{timestamp}_{file_name}")
                shutil.move(src_path, dest_path)
                print(f"Moved '{file_name}' to {dest_path}")

    print("Done")

if __name__ == "__main__":
    main()
