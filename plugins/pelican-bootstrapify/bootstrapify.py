'''
bootstrapify
===================================
This pelican plugin adds css classes to nonstatic html output.

This is especially useful if you want to use bootstrap and want
to add its default classes to your tables and images.
'''

from bs4 import BeautifulSoup
from pelican import signals, contents

BOOTSTRAPIFY_DEFAULT = {
    'table': ['table', 'table-striped'],
    'img': ['img-fluid']
}
BOOTSTRAPIFY_KEY = 'BOOTSTRAPIFY'


def init_default_config(pelican):
    from pelican.settings import DEFAULT_CONFIG

    def update_settings(settings):
        temp = BOOTSTRAPIFY_DEFAULT.copy()
        if BOOTSTRAPIFY_KEY in settings:
            temp.update(settings[BOOTSTRAPIFY_KEY])
        settings[BOOTSTRAPIFY_KEY] = temp
        return settings

    DEFAULT_CONFIG = update_settings(DEFAULT_CONFIG)
    if(pelican):
        pelican.settings = update_settings(pelican.settings)


def replace_in_with(searchterm, soup, attributes):
    for item in soup.select(searchterm):
        attribute_set = set(item.attrs.get('class', []) + attributes)
        item.attrs['class'] = list(attribute_set)


def bootstrapify(content):
    if isinstance(content, contents.Static):
        return

    replacements = content.settings[BOOTSTRAPIFY_KEY]
    soup = BeautifulSoup(content._content, 'html.parser')

    for selector, classes in replacements.items():
        replace_in_with(selector, soup, classes)

    content._content = soup.decode()


def register():
    signals.initialized.connect(init_default_config)
    signals.content_object_init.connect(bootstrapify)
