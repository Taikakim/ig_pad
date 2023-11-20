import os
from PIL import Image

def pad_image_to_16_9(image_path):
    with Image.open(image_path) as im:
        # Calculate the desired size while maintaining the aspect ratio
        width, height = im.size
        aspect_ratio = width / height
        target_aspect_ratio = 16 / 9
        
        # Check which dimension (width or height) should be adjusted
        if aspect_ratio < target_aspect_ratio:
            # Image is too tall, need to add padding to the width
            new_width = int(target_aspect_ratio * height)
            result = Image.new("RGB", (new_width, height), color=(0, 0, 0))
            result.paste(im, ((new_width - width) // 2, 0))
        elif aspect_ratio > target_aspect_ratio:
            # Image is too wide, need to add padding to the height
            new_height = int(width / target_aspect_ratio)
            result = Image.new("RGB", (width, new_height), color=(0, 0, 0))
            result.paste(im, (0, (new_height - height) // 2))
        else:
            # Image already has a 16:9 aspect ratio
            return im
        
        return result

def save_padded_image(image, original_path):
    # Save the padded image
    new_filename = f"padded_{os.path.basename(original_path)}"
    image.save(new_filename)
    print(f"Saved: {new_filename}")

def main():
    files_in_current_directory = os.listdir('.')
    
    for file_name in files_in_current_directory:
        if file_name.lower().endswith('.png'):
            try:
                padded_image = pad_image_to_16_9(file_name)
                save_padded_image(padded_image, file_name)
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    main()
