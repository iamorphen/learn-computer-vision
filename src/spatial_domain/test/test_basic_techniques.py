import os

import numpy as np
from PIL import Image

from src import REPO_ROOT
from src.spatial_domain.basic_techniques import mean, var


RGB_TEST_IMAGE = os.path.join(REPO_ROOT, "img/tokyo_skytree_rgb.jpg")
GS_TEST_IMAGE = os.path.join(REPO_ROOT, "img/tokyo_skytree_grayscale.jpg")


def test_mean():
    """Make sure `mean` is valid Python; don't validate return value."""
    image = np.asarray(Image.open(RGB_TEST_IMAGE))
    m = mean(image)
    assert m.shape == (3,)

    image = np.asarray(Image.open(GS_TEST_IMAGE))
    m = mean(image)
    assert m.shape == (1,)


def test_var():
    """Make sure `var` is valid Python; don't validate return value."""
    image = np.asarray(Image.open(RGB_TEST_IMAGE))
    v = var(image)
    assert v.shape == (3,)

    image = np.asarray(Image.open(GS_TEST_IMAGE))
    v = var(image)
    assert v.shape == (1,)


