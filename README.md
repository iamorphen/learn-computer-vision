# Learn Computer Vision

Educational material for learning computer vision, from rule-based approaches to
machine-learned ones.

## Contributing

1. Install the dependencies: `pip install -r requirements.txt`.
2. Install the linters: `pre-commit install`.
3. Start the development server: `mkdocs serve`.

When working with images, always deal with SVGs. Save SVGs as files in an `img`
folder next to the Markdown file the image is used in or in one of its parent
folders if that image will be used in other Markdown files in that part of the
file tree. Note that paths to images are relative to the Markdown file in which
the image is referenced.

All lines in code blocks must be at most 80 characters.

The `prettier` pre-commit hook will reflow your Markdown. It will ignore code
blocks. If you write math blocks and don't want them reflowed, you can have
`prettier` ignore the block by wrapping the block with

```md
<!-- prettier-ignore-start -->
$$
my_equation = ...
$$
<!-- prettier-ignore-end -->
```
