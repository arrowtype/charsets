# Arrow Type Character Sets

A place to store & share useful starter character sets for type design in RoboFont.

## How to use

In RoboFont, there is a Preferences panel for [defining character sets](https://robofont.com/documentation/how-tos/defining-character-sets/). You can copy-paste a character set like `ATC-en-sp-fr-pt-de.txt` into that.

## Files included

- `ASCII.txt` – A basic ASCII character set, e.g. for sketching new Latin fonts.
- `ATC-en-sp-fr-pt-de.txt` – A basic character set for English, Spanish, French, Portuguese, and German.
  - Adds `.notdef Germandbls dotlessi dotlessj` because these are pretty essential.
  - Also includes arrows (duh).

I’ll post more here soon / as I need them.

## Worth noting

These character sets use names from the [AGL](https://github.com/adobe-type-tools/agl-aglfn) that RoboFont will automatically assign Unicode values to.

These character sets are based on information from the fantastic [Alphabet Type Charset Builder](https://www.alphabet-type.com/tools/charset-builder/). If you need to extend them, this is a very useful resource.

The RoboFont extension [GlyphBrowser](https://github.com/LettError/glyphBrowser) makes it easy to add more glyphs to a font, with unicode values, on an ad hoc basis.

[Production Names](https://robofont.com/documentation/how-tos/using-production-names/) should be assigned to glyphs, to ensure they can be easy to design with but also work in PDFs.
