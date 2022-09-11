# Spatial Domain

## Introduction

The "spatial domain" refers to an image represented as a grid of pixel values.
In this representation, the location `(0, 0)` is the upper left of the image,
the x axis runs across the pixel columns, and the y axis runs down the rows of
the image. In other words, some `(x, y)` corresponds to some `(width, height)`
position. In the image below, the pixel at `(3, 2)` is shown in green, assuming
the pixel in the upper-left corner is `(0, 0)`.

![basic image](img/image_grid.svg)

## The Image as a Function

Assuming the pixels in the image above are encoded as RGB, the pixel at `(3, 2)`
has the value `(0, 255, 0)`, and the pixel at `(0, 0)` maps to the value
`(0, 0, 0)`. So the image $I$ acts as a function

$$
I(x, y) = \text{pixel value at (x, y)}
$$

where the representation and semantics of the pixel value depend on the image
encoding. For example, for grayscale the value may be a single number, for RGB a
3-tuple, and for RGBA a 4-tuple.
