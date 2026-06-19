from utils.image_saver import ImageSaver
from utils.image_preprocessor import ImagePreprocessor


class ImageHandler:

    @staticmethod
    def save_preprocessed_captcha(element):
        filepath = ImageSaver.save_screenshot_of_element(element)

        if filepath is None:
            return None

        return ImagePreprocessor.preprocess_file(filepath)
