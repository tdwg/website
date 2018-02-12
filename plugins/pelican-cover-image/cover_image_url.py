from pelican import signals

def cover_image_url(generator):
    """
    Adds cover_image_url attribute for each article/page, based on cover_image in metadata or DEFAULT_COVER_IMAGE
    Works for local images and URLs
    """

    # Create list of articles_or_pages
    articles = getattr(generator, "articles", [])
    drafts = getattr(generator, "drafts", [])
    pages = getattr(generator, "pages", [])
    hidden_pages = getattr(generator, "hidden_pages", [])
    articles_or_pages = articles + drafts + pages + hidden_pages

    for article_or_page in articles_or_pages:
        # We use the cover_image from the article/page metadata if defined and not empty,
        # otherwise we use the DEFAULT_COVER_IMAGE from the settings.
        if hasattr(article_or_page, "cover_image") and article_or_page.cover_image:
            cover_image = article_or_page.cover_image
        elif "DEFAULT_COVER_IMAGE" in generator.settings:
            cover_image = generator.settings["DEFAULT_COVER_IMAGE"]
        else:
            cover_image = ""

        # Then we set the cover_image_url, either directly from the cover_image (if it starts with http)
        # or by combining the SITEURL + COVER_IMAGES_PATH + cover_image (file name).
        if cover_image:
            if cover_image.startswith("http"):
                cover_image_url = cover_image
            elif "COVER_IMAGES_PATH" in generator.settings:
                cover_image_url = generator.settings["SITEURL"] + "/" + generator.settings["COVER_IMAGES_PATH"] + "/" + cover_image
            else:
                cover_image_url = "1"
        else:
            cover_image_url = "2"

        # Add cover_image_url as attribute to article or page:
        article_or_page.cover_image_url = cover_image_url

def register():
    signals.article_generator_finalized.connect(cover_image_url)
    signals.page_generator_finalized.connect(cover_image_url)
