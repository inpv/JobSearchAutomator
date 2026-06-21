from utils.ocr_result import OCRResult


class OCRResultEvaluator:

    @staticmethod
    def choose_best(results: list[OCRResult]) -> OCRResult | None:

        if not results:
            return None

        return max(
            results,
            key=lambda result: result.confidence
        )
