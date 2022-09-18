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

The standard deviation is the square root of the variance.
