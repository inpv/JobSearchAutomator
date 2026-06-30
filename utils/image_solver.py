from utils.image_handler import ImageHandler
from utils.ocr_result_evaluator import OCRResultEvaluator
from utils.solvers.easy_ocr_solver import EasyOCRSolver


class ImageSolver:

    @staticmethod
    def solve_captcha(element):

        image_path = ImageHandler.save_preprocessed_captcha(element)

        if image_path is None:
            return None

        results = []

        solvers = [
            EasyOCRSolver(),
        ]

        for solver in solvers:

            result = solver.solve(image_path)

            if result:
                results.append(result)

        # Debug
        print(results)

        best = OCRResultEvaluator.choose_best(results)

        if best:
            print(
                f"{best.solver} selected "
                f"({best.confidence:.3f}) "
                f"-> {best.text}"
            )

            return best.text

        return None
