# TDWG website

This repository contains the content and settings for the new TDWG website. It is generated as a static website with [Pelican](http://docs.getpelican.com/).

## Getting started

* **Report**: Found a bug? Have a question? See our [contributing guide](CONTRIBUTING.md).
* **Write**: Want to update a page or fix a typo? See our [contributing guide](CONTRIBUTING.md).
* **Deploy**: Want to render and deploy the site? See our [deployment guide](#deployment).

## Repo structure

...

## Deployment

### Installation

1. Verify Python 3.3+ is installed: `python -V`
2. Install [Pelican](http://docs.getpelican.com/en/stable/install.html) (the static site generator): `pip install pelican`
3. Install the [Python implementation of Markdown](https://pypi.python.org/pypi/Markdown): `pip install markdown`
4. Install [Beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4) (for site search): `pip install beautifulsoup4`
5. Clone the theme repos: `git clone https://github.com/tdwg/tdwg-theme`
6. Clone the website repo: `git clone https://github.com/tdwg/website`

## Build site

1. Navigate to the website directory: `cd website`
2. Build the site:
    * Locally: `pelican -s settings.py`
    * On development server: `pelican -s dev-settings.py`
    * On production server: `pelican -s dev-settings.py`
3. The website is generated in `output/`.

## Contributors

[List of contributors](https://github.com/tdwg/website/contributors)

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
