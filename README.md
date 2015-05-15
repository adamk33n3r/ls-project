# Reveal.js DSL

## How to use
Look in the example file for an....example.

### Input file format

1. Configuration
  - Starts with `$`
2. Styling
  - Name of style starts with `&`
  - Use `bg` for slide background and any other css
3. Slides
  - Starts with `@` followed immediately by an optional style to apply then the
    title of the slide
  - Everything followed is the body
  - If you use two `@` then it will become a child of the main slide.

### Generate presentation

To generate run `./main.py filename`

This will output your presentation into a folder called `output` in the current
folder.

