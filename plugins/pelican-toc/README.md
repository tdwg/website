pelican-toc [![Build Status](https://travis-ci.org/ingwinlu/pelican-toc.svg?branch=master)](https://travis-ci.org/ingwinlu/pelican-toc)
===================================

This plugin generates a table of contents for pelican articles and pages, available for themes via `article.toc`.

# Usage
## requirements
Beautifulsoup4 - install via `pip install beautifulsoup4`
## theme
```
{% if article.toc %}
<div class="col-lg-3 hidden-xs hidden-sm">
    {{article.toc}}
</div>
{% endif %}
```
## article
```
Title: Peeking at erlang/chicagoboss
###Intro
###Chicagoboss Magic
###Result
```
## output
```
<div class="col-lg-3 hidden-xs hidden-sm">
    <div id="toc">
      <ul>
        <li>
          <a href="#" title="Peeking at&nbsp;erlang/chicagoboss">Peeking at&nbsp;erlang/chicagoboss</a>
          <ul>
            <li>
              <a href="#intro" title="Intro">Intro</a>
            </li>
            <li>
              <a href="#chicagoboss-magic" title="Chicagoboss&nbsp;Magic">Chicagoboss&nbsp;Magic</a>
            </li>
            <li>
              <a href="#result" title="Result">Result</a>
            </li>
          </ul>
        </li>
      </ul>
    </div>
</div>
```

## settings
```
TOC = {
    'TOC_HEADERS'       : '^h[1-6]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'true',     # If 'true' include title in toc
}
```
All those settings can be overwritten on a per page/article basis via metadata.
Just use the respective keyword as metadata (example: `toc_headers: ^h[1-4]`)

# Differences between pelican-toc and pelican-extract-toc
`extract-toc` uses a markdown extension to generate a toc and then extract it via beautifulsoup.
This extension generates the toc itself, removing the need to write `[ToC]` in your articles.
There also is a 'health' check on id's which should be generated via markdown.extensions.headerid per default, but somehow don't always end up in the output. 
