neocortex.github.io
-------------------

Use Python 2.

To publish to Github pages:

    pelican content -o output -s pelicanconf.py
    ghp-import output
    git push git@github.com:neocortex/neocortex.github.io.git gh-pages:master

