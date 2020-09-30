# TDWG website amazing project

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

1. Clone the [website repo](https://github.com/tdwg/website): `git clone https://github.com/tdwg/website`
2. Clone the [theme repo](https://github.com/tdwg/tdwg-theme): `git clone https://github.com/tdwg/tdwg-theme`
3. Optional: create a virtual environment (e.g. `conda create -n tdwg python=3.7`) and activate it (e.g. `source activate tdwg`)
4. Verify Python 3.3+ is installed: `python --version`
5. Navigate to the website repo and install the [requirements](requirements.txt) (including [Pelican](http://docs.getpelican.com/en/stable/install.html)): `pip install -r requirements.txt`

### Build site

1. Optional: activate your virtual environment (e.g. `source activate tdwg`)
2. Navigate to the website directory: `cd website`
3. Build the site locally: `pelican -s settings.py`
4. The website is generated in `output/` which you can serve with e.g. `python -m http.server 8000`

## Contributors

[List of contributors](https://github.com/tdwg/website/contributors)

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
