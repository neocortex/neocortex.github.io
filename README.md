neocortex.github.io
-------------------

Use Python 2.

* Edit `pelicanconf.py` to edit main content
* To add Jupyter notebook articles see `content_articles` folder as example
  and rename it to `content`


To publish to Github pages:

    pelican content -o output -s pelicanconf.py
    cp ~/resume/resume.pdf output/
    ghp-import output
    git push git@github.com:neocortex/neocortex.github.io.git gh-pages:master -f

Always work in branch `source`, this is where the source code should be pushed
to. Master contains the code used to build the page.
