import os
from datetime import datetime


class ImageSaver:

    @staticmethod
    def save_screenshot_of_element(element, output_dir="screenshots"):

        if element is None:
            print("No element provided for screenshot")
            return None

        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(output_dir, f"{timestamp}.png")

        element.screenshot(filepath)

        if os.path.exists(filepath):
            print(f"Screenshot saved successfully: {filepath} ({os.path.getsize(filepath)} bytes)")
            return filepath
        else:
            print("Screenshot file was not created")
            return None