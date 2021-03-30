# Arrow Type Character Sets

A place to store & share useful starter character sets for type design in RoboFont.

## How to use

In RoboFont, there is a Preferences panel for [defining character sets](https://robofont.com/documentation/how-tos/defining-character-sets/). You can copy-paste a character set like `ATC-en-sp-fr-pt-de.txt` into that.

## Files included

- `ASCII.txt` – A basic ASCII character set, e.g. for sketching new Latin fonts.
- `ATC-en-sp-fr-pt-de.txt` – A basic character set for English, Spanish, French, Portuguese, and German. Intended for WIP font releases.
  - English, Spanish, French, and Portuguese are all in the top ten most-spoken languages in the world. German is close, and is the most spoken native lanuage in the EU. So, this set makes a solid "MVP" character set for a font. 
  - Even if you only expect a font to be used for English (say, because it’s a beta font or a custom brand font), English requires most of these characters in loan words, and then it barely takes more additional time to fully support many tens of millions of additional people. Obviously, you probably want to add support for more languages before considering a font “done.”
  - Adds `.notdef Germandbls dotlessi dotlessj guilsinglleft guilsinglright` because these are either essential or “free” if you’re making this set already.
  - Adds a few basic currencies: `dollar Euro sterling yen`
  - Leaves out a few slightly-less-common typographic symbols: `dagger daggerdbl section`
  - Also includes arrows (duh).

I’ll post more here soon / as I need them.

## Worth noting

These character sets are based on information from the fantastic [Alphabet Type Charset Builder](https://www.alphabet-type.com/tools/charset-builder/). If you need to extend them, this is a very useful resource.

These character sets use names from the [Glyph Name Formatted Unicode List](https://github.com/LettError/glyphNameFormatter), so that RoboFont will automatically assign Unicode values to them, and so they work in PDFs without further steps.

If you adjust glyph names, [Production Names](https://robofont.com/documentation/how-tos/using-production-names/) should probably be assigned to glyphs, to ensure they can be easy to design with but also work in PDFs (where AGL-format glyph names are required).

The RoboFont extension [GlyphBrowser](https://github.com/LettError/glyphBrowser) makes it easy to add more glyphs to a font, with unicode values, on an ad hoc basis.
