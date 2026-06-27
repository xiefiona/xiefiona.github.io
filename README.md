# Personal site with Pixyll

A minimal Jekyll site using the [Pixyll](https://github.com/johno/pixyll) theme via `remote_theme`.

## Local preview

You can rely on GitHub Pages to build this without a local Ruby setup. If you want to preview locally:

### Using GitHub Actions (recommended)
1) Create a new repo on GitHub and push this folder as `main`.
2) In Settings → Pages, set Source: GitHub Actions.
3) The included workflow `.github/workflows/pages.yml` will build with Jekyll and deploy.
4) Your site URL appears in the Pages environment after the first run.

### Custom domain
- Add a `CNAME` file with your domain, commit, then set the same domain in Settings → Pages.


```bash
# Requires Ruby + Bundler
bundle add jekyll jekyll-paginate jekyll-remote-theme --group "jekyll"
bundle exec jekyll serve
```

## GitHub Pages

### Using GitHub Actions (recommended)
1) Create a new repo on GitHub and push this folder as `main`.
2) In Settings → Pages, set Source: GitHub Actions.
3) The included workflow `.github/workflows/pages.yml` will build with Jekyll and deploy.
4) Your site URL appears in the Pages environment after the first run.

### Custom domain
- Add a `CNAME` file with your domain, commit, then set the same domain in Settings → Pages.


- Push this repo to GitHub.
- In the repository settings, enable GitHub Pages for the `main` branch (root).

### Using GitHub Actions (recommended)
1) Create a new repo on GitHub and push this folder as `main`.
2) In Settings → Pages, set Source: GitHub Actions.
3) The included workflow `.github/workflows/pages.yml` will build with Jekyll and deploy.
4) Your site URL appears in the Pages environment after the first run.

### Custom domain
- Add a `CNAME` file with your domain, commit, then set the same domain in Settings → Pages.

- Your site will be available at `https://<username>.github.io/<repo>/`.

To use a user site (`https://<username>.github.io`), rename the repo to `<username>.github.io`.

## Customize
- Edit `_config.yml` for your name, socials, and description.
- Update `_data/navigation.yml` to add/remove top nav items.
- Put publications in `_data/publications.yml` and they will render automatically.
- Replace `assets/images/headshot.jpg` with your photo.
- Drop `assets/Fiona_Xie_CV.pdf` to enable the CV link.

