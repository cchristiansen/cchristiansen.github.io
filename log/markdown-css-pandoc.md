% Markdown + CSS + Pandoc

*Kære Tøger,*

## Out with the old

The specifications of HTML (and CSS) have greatly matured since the days of
Macromedia Shockwave and `<blink>`{.blink} tags. Even JavaScript has become more sane,
admittedly from a low starting base (see
[wat](https://www.destroyallsoftware.com/talks/wat)). Yet few people today
would propose writing articles in HTML: closing tags are cumbersome, naming
body parts in code seems outdated, angle brackets – despite their winsome
aesthetic – are out.

## KISS principle

**Markdown**, a minimal markup language designed to compile to HTML, is the
favoured replacement to HTML for articles, essays and other long-form writing
amongst current techy scribblers (at least amongst those who have yet to
discover the one true way of Emacs and Org-mode). The syntax is ludicrously
simple and requires no explanation (see the
[primer](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
by GitHub). Write in your preferred text editor, and save it with the extension
`.md`.

> Too easy.

<div class="quoter">-- said some person once.</div>

## Shapeshifting

[**Pandoc**](https://pandoc.org), created by a philosopher named
[John MacFarlane](https://johnmacfarlane.net),
is the best program for converting text files from one format to another. To
convert `input.md` to `output.html`, type the following into your favourite
terminal:

```sh
pandoc input.md -o output.html
```

Those are the basics covered.

## Form and substance

To add pizzazz, we require **Cascading Style Sheets (CSS)**. To include a link
to a CSS stylesheet, use the following option with Pandoc:

```sh
pandoc -s --css style.css input.md -o output.html
```

## That’s all folks!

Das war’s. Of course, there are many rabbit holes one can end up going down,
but remember, the purpose of using Markdown in the first place is to keep as
much syntax (and distraction) away as possible.

Keep writing. 加油！ Any questions, ask me – I’ll gladly answer.

## Postscriptum

The Markdown and CSS of this post are available
[here](./markdown-css-pandoc.md) and [here](../main.css).
To re-create the post, type in the following:

```sh
pandoc -s --css main.css \
markdown-css-pandoc.md -o markdown-css-pandoc.html
```

Note: for the correct fonts to be used, you will need
[RobotoMono](../fonts/Roboto_Mono/RobotoMono-Regular.ttf) and
[EBGaramond](../fonts/EBGaramond-0.016/ttf/EBGaramond12-Regular.ttf)
to be in the relative paths as determined by `font-face` in the CSS file.

<div class="footer">
<center>
<a href="./index.html"><img src="https://christianchristiansen.net/portfolio/yayaya-icon.webp"></a>
<a href="./index.html"><h1>Christian Christiansen.</h1></a>
<div id="postamble" class="status">
<a href="../contact.html"><code>christian.l.christiansen {at} gmail.com</code><br /></a>
</div>
</center>
</div>
