from PIL import Image
from pathlib import Path
import concurrent.futures
import sys

def optimize_image(source_path, dest_path):
    try:
        with Image.open(source_path) as img:
            exif = img.info['exif'] if 'exif' in img.info else None
            
            # Optimize and save
            img.save(dest_path, "JPEG", optimize=True, quality=85, exif=exif)
        return f"Optimized: {source_path.name}"
    except Exception as e:
        return f"Error processing {source_path.name}: {str(e)}"

def main():
    SOURCE_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    DEST_DIR = SOURCE_DIR / "Optimized Images"
    DEST_DIR.mkdir(exist_ok=True)

    image_files = [f for f in SOURCE_DIR.rglob("*") if f.suffix.lower() in ('.jpg', '.jpeg')]

    if not image_files:
        print("No JPEG images found in the specified directory.")
        return

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for source_path in image_files:
            dest_path = DEST_DIR / source_path.relative_to(SOURCE_DIR)
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            futures.append(executor.submit(optimize_image, source_path, dest_path))

        for future in concurrent.futures.as_completed(futures):
            print(future.result())

    print("Optimization process complete.")

if __name__ == "__main__":
    main()
