import os
import threading
from tkinter import Tk, Label, Button, filedialog, messagebox
from rembg import remove
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

# Function to process images in the IMG folder
def process_images():
    input_folder = 'IMG'
    output_folder = 'output'

    # Check if IMG folder exists
    if not os.path.exists(input_folder):
        messagebox.showerror("Error", f"'{input_folder}' folder not found.")
        return

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all images in the IMG folder
    images = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if not images:
        messagebox.showinfo("Info", "No images found in the IMG folder.")
        return

    # Process each image in a thread
    def process_image(filename):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, 'rb') as input_file:
            img_data = input_file.read()

        # Remove background
        result = remove(img_data)

        # Save the result
        with open(output_path, 'wb') as output_file:
            output_file.write(result)

        print(f"Processed {filename}")

    # Use ThreadPoolExecutor to run threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        for image in images:
            executor.submit(process_image, image)

    messagebox.showinfo("Success", f"Processed {len(images)} images successfully!")

# Function to run the processing in a thread
def start_processing():
    threading.Thread(target=process_images).start()

# Create the GUI using Tkinter
def create_gui():
    root = Tk()
    root.title("Background Remover")

    # Create GUI elements
    label = Label(root, text="Click 'Start' to process images in the 'IMG' folder.")
    label.pack(pady=10)

    start_button = Button(root, text="Start", command=start_processing)
    start_button.pack(pady=10)

    exit_button = Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)

    # Start the Tkinter main loop
    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
