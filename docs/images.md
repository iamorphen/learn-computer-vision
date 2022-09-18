# Images

In this work, you'll be loading a lot of images from disk to work with them in
RAM. As images have many encodings (grayscale, RGB, RGBA, CMYK, etc.), they can
also have many representations in memory. The conventions we generally expect in
this material fall into two categories: RGB and grayscale.

## Image Formats

### RGB

For images stored in `numpy` arrays, we expect the array shape to be
`(height, width, num_channels)`, where `num_channels` will be 3. Channel 1 is
the red channel, 2 is the green channel, and 3 is the blue one.

For images tored in Torch tensors, the shape is `(num_channels, height, width)`.

In both cases, the pixel values range from [0, 255] if we are dealing with
integers and [0.0, 1.0] if we're dealing with floating point.

### Grayscale

The same conventions apply for grayscale except that there is no `num_channels`
dimension.

## Sample Images

When following this material, if you want to attempt to reproduce our results
exactly in various exercises, you can use our sample images:

- [tokyo_skytree_rgb.jpg](https://github.com/iamorphen/learn-computer-vision/blob/master/img/tokyo_skytree_rgb.jpg)
- [tokyo_skytree_grayscale.jpg](https://github.com/iamorphen/learn-computer-vision/blob/master/img/tokyo_skytree_grayscale.jpg)

## How to Load Images

There are numerous ways to load images. This material uses numpy and Torch, so
the most important thing is that our loaded images are stored in numpy arrays or
Torch tensors following the semantics outlined above.

Numpy does not have a native image-loading function. Instead, libraries such as
[Pillow](https://pypi.org/project/Pillow/),
[OpenCV](https://pypi.org/project/opencv-python/), and
[matplotlib](https://pypi.org/project/matplotlib/) are often used to load images
into numpy arrays. For example, using Pillow:

```py
import numpy as np
from PIL import Image
i = np.asarray(Image.open("./tokyo_skytree_rgb.jpg"))
print(i.shape())
# (600, 450, 3)
```

Documentation for a particular version of `Image.open` is
[here](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open).
If you load images with OpenCV, note that images are loaded as BGR and not RGB.

`torchvision` provides `read_image`. Documentation for a particular version of
this function is
[here](https://pytorch.org/vision/0.13/generated/torchvision.io.read_image.html).

```py
from torchvision.io import ImageReadMode, read_image
i = read_image("./tokyo_skytree_rgb.jpg", mode=ImageReadMode.RGB)
print(i.shape())
# torch.Size([3, 600, 450])
```

We explicitly pass `ImageReadMode.RGB` to force conversion to RGB in the event
the source image is of a different encoding, such as RGBA.

We encourage you to get comfortable with loading images using the language and
tools you'll follow along with.
