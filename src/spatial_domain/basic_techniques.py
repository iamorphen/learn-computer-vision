import numpy as np
from PIL import Image


def mean(image: np.ndarray) -> np.ndarray:
    """
    Args:
        image (np.ndarray): An image of shape (H, W) or (H, W, C).
    Returns:
        The mean of each channel in `image` as a floating-point value.
    """
    # Add a channel dimension to grayscale images.
    if image.ndim == 2:
        image = np.expand_dims(image, axis=image.ndim)

    return image.mean(axis=(0, 1))


def var(image: np.ndarray) -> np.ndarray:
    """
    Args:
        image (np.ndarray): An image of shape (H, W) or (H, W, C).
    Returns:
        The variance of each channel in `image` as a floating-point value.
    """
    # Add a channel dimension to grayscale images.
    if image.ndim == 2:
        image = np.expand_dims(image, axis=image.ndim)

    return image.var(axis=(0, 1))
