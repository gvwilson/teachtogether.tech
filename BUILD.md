# Building This Book

To rebuild this book:

- `pip install -r requirements.txt` to install required Python packages.
  - You only need to do this if you are rebuilding the bibliography and/or cross-reference database.

- `make bib` to regenerate the Markdown version of the bibliography (`_extras/bib.md`) from the BibTeX version (`files/t3.bib`).
  - You only need to do this if the bibliography has changed.

- `make crossref` to regenerate the JSON cross-reference table (`files/crossref.js`) from the Markdown source files.
  - You only need to do this if there have been changes to section numbering, figure numbering, etc.

- `make site` to create HTML in `_site`.

- `make serve -I` to dynamically regenerate HTML and serve it on `localhost:4000`.

## Design

The design goals for the Jekyll template created for this book were:

1. Source files in GitHub-Flavored Markdown (GFM) rather than LaTeX or some other dialect of Markdown.

2. Site rendered using only Jekyll and the plugins available on GitHub.

3. Markdown should be very simple to edit: every formatting convention should be simple to type and check.

The result is:

- Chapters are stored in `_lessons` and appendices in `_extras`.  The prefixes in front of these names, and the corresponding entries in the `_config.yml` configuration file, tell Jekyll to treat each set of files as a collection so that the template can iterate over them.

- The root directory contains `index.md` (the home page, which is Jekylled) and un-Jekylled versions of the license, the code of conduct, and the citation guide.  `_extras` contains Jekylled versions of these latter three files as well; they are duplicated because many open source projects expect these files in the root directory with these names, but managing them separately proved annoying.

- Sections are given IDs using the syntax `## Section Title {#s:slug-something}`, which translates into an h-heading with an `id` attribute.

- Figures are written out using HTML rather than Markdown because GFM doesn't have a syntax for the HTML5 `figure` element.  The `id` is put in the `figcaption`.

- Bibliographic citations are written `[key](#CITE)`.  The value of `key` must match the key of an entry in `_extras/bib.md`, and the string `#CITE` must be written literally.  The JavaScript in `js/youbou.js` looks for links with `#CITE` as their target and rewrites them.  (Note that it's usual to put square brackets around a citation like this---they aren't added by the JavaScript because some citations reference several entries at once.)

- Glossary references are written as `[term in text](#g:some-key)`, where `term in text` appears in the displayed page and `g:some-key` must be a key in `_extras/gloss.md`.  Again, `js/youbou.js` looks for links whose targets have this prefix and rewrites them.

- Appendix references are written `[s:some-key](#APPENDIX)`; chapters and sections are written similarly, with `#CHAPTER` and `#SECTION` as targets.  `js/youbou.js` uses the data loaded from `files/crossref.js` to turn these into links to the appropriate headings in the appropriate files.

- The file `README.md` is turned into `index.html`, while all other files are turned into `slug/index.html`.  This means that the path from the root `index.html` page to other pages is different from the path from any other page.  To accommodate this, `README.md` sets the value of `root` in its YAML header, and this is then passed into `js/youbou.js` during Jekyll template expansion.

## Miscellaneous

- Diagrams are drawn using [draw.io](http://draw.io) (which can be downloaded and installed for offline use).  Save the `.xml` file in `files`, and then export SVG and PDF into the same directory for use in the online and print versions of the book respectively.

- `_includes/toc-section.html` uses a double loop to match collection items to the ordered list in the configuration table of contents.  Since this is run once for each file, the process is actually N^3, which is nuts, but Jekyll doesn't have a way to force ordering of a collection or to turn a collection into a lookup table with a user-defined key.  <https://github.com/jekyll/jekyll/pull/5904> was supposed to fix this, but...
