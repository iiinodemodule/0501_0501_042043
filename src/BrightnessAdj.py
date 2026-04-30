import torch


def adjust_brightness(image, strength):
    # 變數名稱必須與 INPUT_TYPES 中宣告的名稱一致
    # image 為 torch.Tensor，shape: [B, H, W, C]
    result = torch.clamp(image * strength, 0.0, 1.0)

    # 回傳值必須是 Tuple 格式
    return (result,)