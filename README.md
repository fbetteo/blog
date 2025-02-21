https://fbetteo.github.io/blog

To develop:
`mkdocs serve`

```bash
conda activate mkdocs-blog
```

To deploy:
Checkout to "main"
```bash 
# mkdocs build
mkdocs gh-deploy
```

TO INCLUDE SITEMAP
```bash
mkdocs build
python generate_sitemap.py
ghp-import -n -p site
```
Deploy Using ghp‑import

Run the following command to push the contents of your site/ folder to GitHub Pages:

`ghp-import -n -p site`
The -n flag adds a .nojekyll file so that GitHub Pages doesn’t try to process your site with Jekyll.
The -p flag pushes the changes to the gh-pages branch automatically.
This way, you deploy exactly what’s in your site/ folder—including your custom sitemap—without gh‑deploy rebuilding the site and overwriting your changes.