import os
import sys
import torch

SRC_DIR = os.path.join(os.path.dirname(__file__), "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

_import_error = None
try:
    from BrightnessAdj import adjust_brightness
except Exception as _e:
    adjust_brightness = None
    _import_error = f"{type(_e).__name__}: {_e}"


class CustomAlgorithmNew_Node_0501_042043Node:
    CATEGORY = "0501_042043自訂演算法/T"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01})
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output",)
    FUNCTION = "process_data"

    def process_data(self, image, strength):
        if adjust_brightness is None:
            raise RuntimeError(f"無法匯入來源程式碼。原因: {_import_error}")
        result = adjust_brightness(image, strength)
        if not isinstance(result, tuple):
            result = (result,)
        return result
