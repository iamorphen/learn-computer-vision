# Basic Techniques Solutions

## Mean and Variance

```py
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
```

We choose to use numpy utilities to compute the mean and variance. If you also
choose to use numpy but are not familiar with it, we recommend you spend some
time to learn how to operate on numpy arrays. Regarding the code above, we first
add a channel dimension if the input image has no channel information, and then
we compute the mean or variance and return an array of shape `(num_channels,)`.
We compute the mean or variance across the height and width of the image for
each channel by specifying `axis=(0, 1)`. See the numpy documentation for an
explanation of how the `axis` parameter works. Also, the numpy glossary on
[`axis`](https://numpy.org/doc/stable/glossary.html#term-axis) is useful to read
to learn how axes are arranged and indexed into.
