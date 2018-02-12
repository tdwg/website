# GitHub edit URL

A [Pelican](http://getpelican.com/) plugin that adds a `github_edit_url` attribute to articles and pages, similar to [Read the Docs](http://docs.getpelican.com/en/latest/index.html) pages.

## Installation

1. Download this plugin
2. Place it in your plugins directory
3. Add `github_edit_url` to `PLUGINS` in your settings file.

Or see the general [Plugin installation instructions](http://docs.getpelican.com/en/latest/plugins.html).

## Usage

Add the URL of your public website repository (including the path to the content directory) to your settings file:

```python
GITHUB_CONTENT_URL = "https://github.com/your_user_name/your_website_repo/blob/master/your_content_dir" # No trailing slash
```

This will active the `github_edit_url` attribute for all articles and pages, which you can use in templates as follows:

**Article template:**

```html
<a href={{ article.github_edit_url }}>Edit on GitHub</a>
```

**Page template:**

```html
<a href={{ page.github_edit_url }}>Edit on GitHub</a>
```

## LICENSE

[LICENSE](LICENSE) 
