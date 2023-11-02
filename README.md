# TDWG website

[![Build Status](https://builds.gbif.org/job/tdwg-website/badge/icon?style=flat-square)](https://builds.gbif.org/job/tdwg-website/)

This repository contains the source files for the [TDWG website](https://www.tdwg.org/).

## Usage

This website makes use of the static website generator [Jekyll](https://jekyllrb.com/) and the [Petridish](https://github.com/peterdesmet/petridish) theme. **Each commit to `master` will automatically trigger a new build by [Jenkins](https://builds.gbif.org/job/tdwg-website/)** (maintained by GBIF) and update the website. There is no need to build the site locally, but you can by installing Jekyll and running `bundle exec jekyll serve`.

Found a typo, have a question? See our [contributing guide](https://www.tdwg.org/about/website-faq/).

## Repo structure

The repository structure follows that of Jekyll websites.

- General site settings: [_config.yml](_config.yml)
- Pages: `index.md` files in (sub)directories such as [about/](about/) and [community/](community/).
- Posts: [_posts/](_posts/)
- Images & static files: [assets/](assets/)
- Top navigation: [_data/navigation.yml](_data/navigation.yml)
- Footer content: [_data/footer.yml](_data/footer.yml)

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
