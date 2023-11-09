import torch
from torch.nn.functional import grid_sample


from typing import List
import math

# from torchvision.transforms.v2.functional._geometry import _get_inverse_affine_matrix
def _get_inverse_affine_matrix(
    center: List[float], angle: float, translate: List[float], scale: float, shear: List[float], inverted: bool = True
) -> List[float]:
    # Helper method to compute inverse matrix for affine transformation

    # Pillow requires inverse affine transformation matrix:
    # Affine matrix is : M = T * C * RotateScaleShear * C^-1
    #
    # where T is translation matrix: [1, 0, tx | 0, 1, ty | 0, 0, 1]
    #       C is translation matrix to keep center: [1, 0, cx | 0, 1, cy | 0, 0, 1]
    #       RotateScaleShear is rotation with scale and shear matrix
    #
    #       RotateScaleShear(a, s, (sx, sy)) =
    #       = R(a) * S(s) * SHy(sy) * SHx(sx)
    #       = [ s*cos(a - sy)/cos(sy), s*(-cos(a - sy)*tan(sx)/cos(sy) - sin(a)), 0 ]
    #         [ s*sin(a - sy)/cos(sy), s*(-sin(a - sy)*tan(sx)/cos(sy) + cos(a)), 0 ]
    #         [ 0                    , 0                                      , 1 ]
    # where R is a rotation matrix, S is a scaling matrix, and SHx and SHy are the shears:
    # SHx(s) = [1, -tan(s)] and SHy(s) = [1      , 0]
    #          [0, 1      ]              [-tan(s), 1]
    #
    # Thus, the inverse is M^-1 = C * RotateScaleShear^-1 * C^-1 * T^-1

    rot = math.radians(angle)
    sx = math.radians(shear[0])
    sy = math.radians(shear[1])

    cx, cy = center
    tx, ty = translate

    # Cached results
    cos_sy = math.cos(sy)
    tan_sx = math.tan(sx)
    rot_minus_sy = rot - sy
    cx_plus_tx = cx + tx
    cy_plus_ty = cy + ty

    # Rotate Scale Shear (RSS) without scaling
    a = math.cos(rot_minus_sy) / cos_sy
    b = -(a * tan_sx + math.sin(rot))
    c = math.sin(rot_minus_sy) / cos_sy
    d = math.cos(rot) - c * tan_sx

    if inverted:
        # Inverted rotation matrix with scale and shear
        # det([[a, b], [c, d]]) == 1, since det(rotation) = 1 and det(shear) = 1
        matrix = [d / scale, -b / scale, 0.0, -c / scale, a / scale, 0.0]
        # Apply inverse of translation and of center translation: RSS^-1 * C^-1 * T^-1
        # and then apply center translation: C * RSS^-1 * C^-1 * T^-1
        matrix[2] += cx - matrix[0] * cx_plus_tx - matrix[1] * cy_plus_ty
        matrix[5] += cy - matrix[3] * cx_plus_tx - matrix[4] * cy_plus_ty
    else:
        matrix = [a * scale, b * scale, 0.0, c * scale, d * scale, 0.0]
        # Apply inverse of center translation: RSS * C^-1
        # and then apply translation and center : T * C * RSS * C^-1
        matrix[2] += cx_plus_tx - matrix[0] * cx - matrix[1] * cy
        matrix[5] += cy_plus_ty - matrix[3] * cx - matrix[4] * cy

    return matrix


from torch import Tensor

# from torchvision.transforms._functional_tensor import _gen_affine_grid
def _gen_affine_grid(
    theta: Tensor,
    w: int,
    h: int,
    ow: int,
    oh: int,
) -> Tensor:
    # https://github.com/pytorch/pytorch/blob/74b65c32be68b15dc7c9e8bb62459efbfbde33d8/aten/src/ATen/native/
    # AffineGridGenerator.cpp#L18
    # Difference with AffineGridGenerator is that:
    # 1) we normalize grid values after applying theta
    # 2) we can normalize by other image size, such that it covers "extend" option like in PIL.Image.rotate

    d = 0.5
    base_grid = torch.empty(1, oh, ow, 3, dtype=theta.dtype, device=theta.device)
    x_grid = torch.linspace(-ow * 0.5 + d, ow * 0.5 + d - 1, steps=ow, device=theta.device, dtype=theta.dtype)
    base_grid[..., 0].copy_(x_grid)
    y_grid = torch.linspace(-oh * 0.5 + d, oh * 0.5 + d - 1, steps=oh, device=theta.device, dtype=theta.dtype).unsqueeze_(-1)
    base_grid[..., 1].copy_(y_grid)
    base_grid[..., 2].fill_(1)

    rescaled_theta = theta.transpose(1, 2) / torch.tensor([0.5 * w, 0.5 * h], dtype=theta.dtype, device=theta.device)
    output_grid = base_grid.view(1, oh * ow, 3).bmm(rescaled_theta)
    return output_grid.view(1, oh, ow, 2)


dtype = torch.float32
# dtype = torch.float64
# angle = 56.0
mode = "bilinear"
# mode = "nearest"

orig_img = torch.ones(1, 3, 46, 46, dtype=dtype)
orig_img[:, 1, ...] = 0.0
orig_img[:, 2, ...] = 0.0
mask = torch.ones((orig_img.shape[0], 1, orig_img.shape[2], orig_img.shape[3]), dtype=orig_img.dtype, device=orig_img.device)
img = torch.cat((orig_img, mask), dim=1)

# center_f = [0.0, 0.0]
# matrix = _get_inverse_affine_matrix(center_f, -angle, [0.0, 0.0], 1.0, [0.0, 0.0])

# w, h = img.shape[-1], img.shape[-2]
# ow, oh = w, h
# dtype = img.dtype if torch.is_floating_point(img) else torch.float32
# theta = torch.tensor(matrix, dtype=dtype, device=img.device).reshape(1, 2, 3)
# grid = _gen_affine_grid(theta, w=w, h=h, ow=ow, oh=oh)

n, c, w, h = img.shape
grid = torch.rand(n, h, w, 2, dtype=dtype)

out = grid_sample(img, grid, mode=mode, padding_mode="zeros", align_corners=False)
mask = out[:, -1:, :, :]  # N * 1 * H * W
out = out[:, :-1, :, :]  # N * C * H * W

torch.set_printoptions(precision=16)
print("Unique:", mask.unique())

mask = mask[0, 0, ...]
m = (mask > 0.999) & (mask < 1.0)
print(mask[m])
print(torch.where(m))

# m = mask[0, 0, ...].clone()
# m[m < 0.999] = 0
# print("m", m)
