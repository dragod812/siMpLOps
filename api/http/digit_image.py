from pydantic import BaseModel
from typing import List
import numpy as np


class DigitImage(BaseModel):
    image: List[float] = None

    def to_numpy(self):
        return np.array(self.image).astype(np.float32)
