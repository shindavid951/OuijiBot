import PIL.Image
import os

poisoned = PIL.Image.open("./status_images/poisoned.png")
forgotten = PIL.Image.open("./status_images/forgotten.png")
depressed = PIL.Image.open("./status_images/depressed.png")

folder_path = "./card_images"

for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        image_path = os.path.join(folder_path, filename)
        with PIL.Image.open(image_path) as img:
            poisoned_img = img.copy()
            forgotten_img = img.copy()
            depressed_img = img.copy()
            poisoned_img.paste(poisoned, (int(((poisoned_img.size[0] / 2) - (poisoned.size[0] / 2))), 100), mask=poisoned)
            forgotten_img.paste(forgotten, (int(((forgotten_img.size[0] / 2) - (forgotten.size[0] / 2))), 100), mask=forgotten)
            depressed_img.paste(depressed, (int(((depressed_img.size[0] / 2) - (depressed.size[0] / 2))), 100), mask=depressed)
            poisoned_img.save(os.path.join(folder_path, f"Poisoned{filename}"), "PNG")
            forgotten_img.save(os.path.join(folder_path, f"Forgotten{filename}"), "PNG")
            depressed_img.save(os.path.join(folder_path, f"Depressed{filename}"), "PNG")