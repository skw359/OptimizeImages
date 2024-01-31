from PIL import Image
import os

SOURCE_DIR = ""
DEST_DIR = os.path.join(SOURCE_DIR, "Optimized Images")

if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)

def optimize_image(file_path, save_path):
    with Image.open(file_path) as img:
        img.save(save_path, "JPEG", optimize=True)

def main():
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg"):
                dest_file_path = os.path.join(DEST_DIR, file)
                source_file_path = os.path.join(root, file)
                optimize_image(source_file_path, dest_file_path)
                print(f"Optimized and saved {file} to 'Optimized Images' folder")

if __name__ == "__main__":
    main()
