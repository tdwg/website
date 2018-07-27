# TDWG website

This repository contains the content and settings for the new TDWG website. It is generated as a static website with [Pelican](http://docs.getpelican.com/).

## Getting started

* **Report**: Found a bug? Have a question? See our [contributing guide](.github/CONTRIBUTING.md).
* **Write**: Want to update a page or fix a typo? See our [contributing guide](.github/CONTRIBUTING.md).
* **Deploy**: Want to render and deploy the site? See our [deployment guide](#deployment).

## Repo structure

```
```

## Deployment

[tdwg.org](https://www.tdwg.org) is rebuilt automatically for any change on the `master` branch in [this repository](https://github.com/tdwg/website) or the [tdwg-theme repository](https://github.com/tdwg/tdwg-theme). You can see the status of the builds at <https://builds.gbif.org/job/tdwg-website/>. If you want to build the website locally, do the following:

### Installation

1. Verify Python 3.3+ is installed: `python -V`
2. Install [Pelican](http://docs.getpelican.com/en/stable/install.html) (the static site generator): `pip install pelican`
3. Install the [Python implementation of Markdown](https://pypi.python.org/pypi/Markdown): `pip install markdown`
4. Install [Beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4) (for site search): `pip install beautifulsoup4`
5. Clone the theme repo: `git clone https://github.com/tdwg/tdwg-theme`
6. Clone the website repo: `git clone https://github.com/tdwg/website`

### Build site

1. Navigate to the website directory: `cd website`
2. Build the site locally: `pelican -s settings.py`
3. The website is generated in `output/` which you can serve with e.g. `python -m http.server 8000`

## Contributors

[List of contributors](https://github.com/tdwg/website/contributors)

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
