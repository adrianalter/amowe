## Chapter 1: Introduction to HTML Basics

This chapter covers the fundamental building blocks of HTML (Hypertext Markup Language), the standard language for creating web pages.

### HTML Page Structure

A basic HTML document follows this structure:

* **`<!DOCTYPE html>`:** Declares the document type and HTML version.
* **`<html>`:** The root element of the page.
* **`<head>`:** Contains meta information about the document.
  * **`<title>`:** Defines the page title, displayed in the browser tab or title bar.
* **`<body>`:** Contains the visible content, like text, images, and other media.
  * **`<h1>`:** Defines a large heading.
  * **`<p>`:** Defines a paragraph.
  * **`<br>`:** Inserts a line break (empty element, no closing tag needed).

### Hyperlinks

```html
<a href="https://www.w3schools.com">This is a link</a>
```

* The `<a>` tag defines a hyperlink.
* The `href` attribute specifies the target URL of the link.

### Images

```html
<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
```

* The `<img>` tag embeds an image.
* Attributes:
  * `src`: path to the image file.
  * `alt`: alternative text for accessibility.
  * `width` and `height`: image size in pixels (optional).

### Empty Elements

Elements like `<br>` (line break) have no content and don't require closing tags.

### URL Types in `src` Attribute

* **Absolute URL:** Links to an image hosted elsewhere, e.g., `src="https://www.example.com/image.jpg"`.
* **Relative URL:** Links to an image within the same website, e.g., `src="image.jpg"` or `src="/images/image.jpg"`.

### `alt`, `width`, `height`, and `lang` Attributes

* `alt`: essential for accessibility, providing text alternatives for images.
* `width` and `height`: define image size.
* `lang` in the `<html>` tag declares the page language for search engines and browsers.

### The `title` Attribute

* Provides additional information about an element, displayed as a tooltip on mouseover.

Example:

```html
<p title="I'm a tooltip">This is a paragraph.</p>
```

## Chapter 1 Summary

This chapter explored the fundamentals of HTML, including:

* Basic document structure.
* Headings, paragraphs, links, and images.
* Empty elements like `<br>`.
* Absolute vs. relative URLs in the `src` attribute.
* The importance of `alt`, `width`, `height`, `lang`, and `title` attributes.

Understanding these elements lays the foundation for creating structured, accessible, and efficient web pages.

---

## Chapter 2: Advanced HTML Features

Building on the basics, this chapter explores more advanced HTML features, including applying styles with the `style` attribute and CSS properties.

### Enhancing Headings

Adjust heading size using the `style` attribute and the `font-size` CSS property:

```html
<h1 style="font-size:60px;">Bigger Heading</h1>
```

### Horizontal Lines

The `<hr>` tag creates thematic breaks, often displayed as a horizontal line, separating content or indicating page changes:

```html
<h1>Heading 1</h1>
<p>Text content.</p>
<hr>
<h2>Heading 2</h2>
<p>More text content.</p>
<hr>
```

### Preformatted Text with `<pre>`

The `<pre>` element is for preformatted text, preserving spaces and line breaks, typically displayed in a fixed-width font:

```html
<pre>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.

  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</pre>
```

### Inline HTML Styling

The `style` attribute applies CSS styles to individual elements:

```html
<tagname style="property:value;">
```

`property` is a CSS property, and `value` is its corresponding value.

### Background Colors

The `background-color` CSS property sets the background color:

```html
<body style="background-color:powderblue;">
```

Example of setting different background colors:

```html
<body>
<h1 style="background-color:powderblue;">Heading</h1>
<p style="background-color:tomato;">Paragraph</p>
</body>
```

## Chapter 2 Summary

This chapter introduced:

* Using the `style` attribute for inline styling with CSS properties.
* The `<hr>` tag for thematic breaks.
* The `<pre>` element for preformatted text.
* Applying background colors to elements.

These features enhance the ability to create visually appealing and well-structured web pages.

---

## Chapter 3: Styling Text in HTML

This chapter delves into styling text within HTML documents using CSS properties and explores HTML formatting elements for text decoration.

### Text Color Control

The `color` CSS property defines text color:

```html
<h1 style="color:blue;">Heading</h1>
<p style="color:red;">Paragraph</p>
```

### Font Customization

The `font-family` CSS property specifies the font:

```html
<h1 style="font-family:verdana;">Heading</h1>
<p style="font-family:courier;">Paragraph</p>
```

### Adjusting Text Size

Use the `font-size` CSS property to control text size:

```html
<h1 style="font-size:300%;">Larger Heading</h1>
<p style="font-size:160%;">Bigger Paragraph</p>
```

### Text Alignment

The `text-align` CSS property sets horizontal text alignment:

```html
<h1 style="text-align:center;">Centered Heading</h1>
<p style="text-align:center;">Centered Paragraph</p>
```

### HTML Formatting Elements

HTML provides elements for specific text formatting:

- `<b>`: Bold text.
- `<strong>`: Important text (also bold).
- `<i>`: Italic text.
- `<em>`: Emphasized text (typically italic).
- `<mark>`: Highlighted text.
- `<small>`: Reduced text size.
- `<del>`: Deleted text.
- `<ins>`: Inserted text.
- `<sub>`: Subscript text.
- `<sup>`: Superscript text.

These elements allow semantic markup of text, indicating meaning and emphasis changes beyond just styling.

## Chapter 3 Summary

This chapter covered:

* Text styling with CSS properties like `color`, `font-family`, `font-size`, and `text-align`.
* HTML formatting elements for semantic and visual marking of text.

Understanding and applying these elements and properties enable the creation of more readable, accessible, and visually appealing web content.

Remember to replace these summaries and examples with your actual content from Chapters 2 and 3 for a complete .md file.

---

## Chapter 4: What is CSS?

### Introduction

This chapter covers the basics of Cascading Style Sheets (CSS), a language used to format the layout and presentation of web pages. 

### What is CSS?

CSS stands for Cascading Style Sheets. It allows you to control various aspects of a webpage's appearance, including:

* **Color:** Change the color of text, backgrounds, and other elements.
* **Fonts:** Specify the font family, size, and other font properties.
* **Spacing:** Control the space between elements and around content.
* **Positioning:** Arrange elements on the page in specific locations.
* **Layout:** Define the overall structure and layout of the page.
* **Backgrounds:** Add images or colors to the background of elements.
* **Device Responsive Design:** Create pages that adapt to different screen sizes and devices.

### Applying CSS

You can add CSS to HTML documents in three ways:

**1. Inline:** This method uses the `style` attribute directly within HTML elements for unique styling.

**2. Internal:** Define styles within a `<style>` element in the `<head>` section of the HTML page.

**3. External:** Create a separate CSS file (`.css` extension) and link it to the HTML page using a `<link>` element in the `<head>` section. This is the preferred method for large stylesheets.

### Inline and Internal CSS Examples

#### Inline CSS

```html
<h1 style="color: blue;">A Blue Heading</h1>
<p style="color: red;">A red paragraph.</p>
```

#### Internal CSS

```html
<!DOCTYPE html>
<html>
<head>
<style>
body { background-color: powderblue; }
h1   { color: blue; }
p    { color: red; }
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

### External CSS Example

**HTML:**

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

**CSS (styles.css):**

```css
body {
  background-color: powderblue;
}
h1 {
  color: blue;
}
p {
  color: red;
}
```

### Basic CSS Properties

Here are some common CSS properties with examples:

**Color:**

```css
color: blue;
```

**Font:**

```css
font-family: verdana;
font-size: 300%;
```

**Border:**

```css
border: 2px solid powderblue;
```

**Padding:**

```css
padding: 30px;
```

**Margin:**

```css
margin: 50px;
```

### Linking with Full URL or Relative Path

**Full URL:**

```html
<link rel="stylesheet" href="https://www.w3schools.com/html/styles.css">
```

**Relative Path:**

```html
<link rel="stylesheet" href="styles.css">
```

---

Chapter 5
Image as a Link
To use an image as a link, put the <img> tag inside the <a> tag:

Example
<a href="default.asp">
  <img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;">
</a>

Image Floating
Use the CSS float property to let the image float to the right or to the left of a text:

Example
<p><img src="smiley.gif" alt="Smiley face" style="float:right;width:42px;height:42px;">
The image will float to the right of the text.</p>

<p><img src="smiley.gif" alt="Smiley face" style="float:left;width:42px;height:42px;">
The image will float to the left of the text.</p>