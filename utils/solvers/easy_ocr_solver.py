import easyocr
from utils.ocr_result import OCRResult


class EasyOCRSolver:

    _reader = easyocr.Reader(
        ["ru"],
        gpu=False
    )

    _ALLOWLIST = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "

    @classmethod
    def solve(cls, image_path):

        result = cls._reader.readtext(image_path,
                                      allowlist=cls._ALLOWLIST)

        if not result:
            return None

        texts = []
        confidences = []

        for detection in result:
            texts.append(detection[1])
            confidences.append(detection[2])

        return OCRResult(
            text=" ".join(texts).strip(),
            confidence=sum(confidences) / len(confidences),
            solver="EasyOCR"
        )
