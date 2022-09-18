# Basic Techniques

## Introduction

We can compute some basic statistics on images to measure certain
characteristics about them. Some of these measurements come in handy when
comparing different parts of the same image with each other or when comparing
two unique images.

For the sections below, consider a grayscale image $I$ that has $N_{cols}$ and
$M_{rows}$.

## Basic Statistics

The mean of an image is the mean of all of its pixel values.

<!-- prettier-ignore-start -->
$$
\displaystyle \mu_I = {{ 1 \over {N_{cols} \times M_{rows}}} \times \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{M_{rows}} I(x, y) }
$$
<!-- prettier-ignore-end -->

The variance is

<!-- prettier-ignore-start -->
$$
\displaystyle \sigma_I^2 = {{ 1 \over {N_{cols} \times M_{rows}}} \times \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{M_{rows}} [I(x, y) - \mu_I]^2 }
$$
<!-- prettier-ignore-end -->

From statistics, we know that the standard deviation is the square root of the
variance.

## Challenge

To get comfortable with working with images in your language and tooling of
choice, implement two functions, one to compute the mean of an image and another
to compute the variance. Whether to do the math yourself or use your math
library's utility functions is up to you. Consider how you might report these
measurements for RGB images and grayscale images.

Example solutions are [here](./basic_techniques_solutions.md).
