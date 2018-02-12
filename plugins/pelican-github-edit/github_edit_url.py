from pelican import signals

def github_edit_url(generator):
    """
    Adds github_edit_url attribute for each article/page from 
    GITHUB_CONTENT_URL + local source_path
    """

    if "GITHUB_CONTENT_URL" in generator.settings: # Required setting
        # Create list of articles_or_pages
        articles = getattr(generator, "articles", []) # Populated if called from ArticleGenerator
        pages = getattr(generator, "pages", [])       # Populated if called from PageGenerator
        articles_or_pages = articles + pages

        # Add github_edit_url as attribute to article or page:
        for article_or_page in articles_or_pages:
            # Articles and pages have attribute source_path:    /Users/.../pelican_dir/content_dir/.../file.md
            # PATH is path to content dir or working directory: /Users/.../pelican_dir/content_dir
            # Substracting one from the other gets short_source_path:                             /.../file.md
            short_source_path = article_or_page.source_path.replace(generator.settings["PATH"],"")

            # Prepend with GITHUB_CONTENT_URL to create full URL
            article_or_page.github_edit_url = generator.settings["GITHUB_CONTENT_URL"] + short_source_path

def register():
    signals.article_generator_finalized.connect(github_edit_url)
    signals.page_generator_finalized.connect(github_edit_url)
