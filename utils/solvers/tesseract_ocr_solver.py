import pytesseract
from PIL import Image
from utils.ocr_result import OCRResult


class TesseractOCRSolver:

    @classmethod
    def solve(cls, image_path):

        image = Image.open(image_path)

        data = pytesseract.image_to_data(
            image,
            lang="rus",
            config=(
                "--oem 3 "
                "--psm 8 "
                "-c tessedit_char_whitelist="
                "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
            ),
            output_type=pytesseract.Output.DICT
        )

        words = []
        confidences = []

        for text, conf in zip(data["text"], data["conf"]):
            text = text.strip()

            if not text:
                continue

            try:
                conf = float(conf)
            except ValueError:
                continue

            words.append(text)
            confidences.append(conf)

        if not words:
            return None

        confidence = sum(confidences) / len(confidences)

        return OCRResult(
            text=" ".join(words),
            confidence=confidence / 100.0,
            solver="Tesseract"
        )