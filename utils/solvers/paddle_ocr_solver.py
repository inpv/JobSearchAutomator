from paddleocr import PaddleOCR
from utils.ocr_result import OCRResult


class PaddleOCRSolver:

    _ocr = PaddleOCR(
        lang="ru",
        text_recognition_model_name="eslav_PP-OCRv5_mobile_rec",
        use_textline_orientation=True,
        device="cpu",
        enable_mkldnn=False
    )

    @classmethod
    def solve(cls, image_path):

        result = cls._ocr.ocr(image_path)

        if not result or not result[0]:
            return None

        texts = []
        confidences = []

        # Debug
        print("Raw result type:", type(result))
        print("Raw result:", result)

        for page_result in result:
            if isinstance(page_result, dict):
                # New format
                rec_texts = page_result.get('rec_texts', [])
                rec_scores = page_result.get('rec_scores', [])

                texts.extend(rec_texts)
                confidences.extend([float(s) for s in rec_scores if isinstance(s, (int, float))])

            elif isinstance(page_result, list):
                # Fallback
                for line in page_result:
                    if isinstance(line, (list, tuple)) and len(line) >= 2:
                        word_info = line
                        detected_text = word_info[1][0] if isinstance(word_info[1], (list, tuple)) else str(
                            word_info[1])
                        texts.append(detected_text)

                        try:
                            conf = word_info[1][1] if isinstance(word_info[1], (list, tuple)) else 0.0
                            confidences.append(float(conf))
                        except (IndexError, TypeError):
                            confidences.append(0.0)
            else:
                continue

        if not texts:
            return None

        avg_conf = sum(confidences) / len(confidences) if confidences else 0.0

        return OCRResult(
            text=" ".join(texts).strip(),
            confidence=avg_conf,
            solver="PaddleOCR"
        )
