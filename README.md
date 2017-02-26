neocortex.github.io
-------------------

Use Python 2.

To publish to Github pages:

    pelican content -o output -s pelicanconf.py
    cp ~/resume/resume.pdf output/
    ghp-import output
    git push git@github.com:neocortex/neocortex.github.io.git gh-pages:master -f

Source code is in branch `source`, master contains the code used to build the page.
