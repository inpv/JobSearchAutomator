from dataclasses import dataclass


@dataclass(slots=True)
class OCRResult:
    text: str
    confidence: float
    solver: str
