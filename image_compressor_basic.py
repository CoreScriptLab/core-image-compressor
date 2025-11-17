from PIL import Image
import os

def compress_images(input_folder, output_folder, quality=70, max_size=(1280, 1280)):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(image_path) as img:
                img.thumbnail(max_size)
                img.save(output_path, optimize=True, quality=quality)

            print(f"Compressed: {filename}")

    print("Done!")

if __name__ == "__main__":
    inp = input("Input folder: ")
    outp = input("Output folder: ")
    compress_images(inp, outp)
