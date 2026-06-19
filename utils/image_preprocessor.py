import cv2


class ImagePreprocessor:

    @staticmethod
    def preprocess_image(image):
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()

        clahe = cv2.createCLAHE(
            clipLimit=3.0,
            tileGridSize=(8, 8)
        )

        gray = clahe.apply(gray)

        gray = cv2.bilateralFilter(gray, 9, 75, 75)

        binary = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            41,
            15
        )

        return binary

    @staticmethod
    def preprocess_file(filepath):
        image = cv2.imread(filepath)

        if image is None:
            raise ValueError(f"Could not read image: {filepath}")

        processed = ImagePreprocessor.preprocess_image(image)

        cv2.imwrite(filepath, processed)

        return filepath
