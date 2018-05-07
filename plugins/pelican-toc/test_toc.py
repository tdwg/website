from io import open

import unittest
import re
import toc

from pelican.readers import MarkdownReader
from pelican.contents import Article
from pelican.tests.support import get_settings


class TestToCGeneration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        toc.init_default_config(None)
        cls.settings = get_settings()
        cls.md_reader = MarkdownReader(cls.settings)

    def setUp(self):
        # have to reset the default, because shallow copies
        self.settings['TOC']['TOC_HEADERS'] = '^h[1-6]'
        self.settings['TOC']['TOC_RUN'] = 'true'
        self.maxDiff = 9999

    def _handle_article_generation(self, path):
        content, metadata = self.md_reader.read(path)
        return Article(content=content, metadata=metadata)

    def _generate_toc(self, article_path, expected_path):
        result = self._handle_article_generation(article_path)
        toc.generate_toc(result)
        expected = ""
        with open(expected_path, 'r') as f:
            expected = f.read()
        return result, expected

    def test_toc_generation(self):
        self.settings['TOC']['TOC_INCLUDE_TITLE'] = 'true'
        result, expected = self._generate_toc(
                "test_data/article_with_headers.md",
                "test_data/article_with_headers_toc.html"
            )
        self.assertEqual(result.toc, expected)

    def test_toc_generation_nonascii(self):
        self.settings['TOC']['TOC_INCLUDE_TITLE'] = 'true'
        result, expected = self._generate_toc(
                "test_data/article_with_headers_nonascii.md",
                "test_data/article_with_headers_toc_nonascii.html"
            )
        self.assertEqual(result.toc, expected)

    def test_toc_generation_exclude_small_headers(self):
        self.settings['TOC']['TOC_INCLUDE_TITLE'] = 'true'
        self.settings['TOC']['TOC_HEADERS'] = '^h[1-3]'
        result, expected = self._generate_toc(
            "test_data/article_with_headers_exclude_small_headers.md",
            "test_data/article_with_headers_toc_exclude_small_headers.html"
        )
        self.assertEqual(result.toc, expected)

    def test_toc_generation_exclude_small_headers_metadata(self):
        self.settings['TOC']['TOC_INCLUDE_TITLE'] = 'true'
        result, expected = self._generate_toc(
            "test_data/article_with_headers_exclude_small_headers_metadata.md",
            "test_data/article_with_headers_toc_exclude_small_headers.html"
        )
        self.assertEqual(result.toc, expected)


    def test_bad_TOC_HEADERS(self):
        self.settings['TOC']['TOC_INCLUDE_TITLE'] = 'true'
        self.settings['TOC']['TOC_HEADERS'] = '^[1-'
        with self.assertRaises(re.error):
            self._generate_toc(
                "test_data/article_with_headers_exclude_small_headers.md",
                "test_data/article_with_headers_toc_exclude_small_headers.html"
            )

    def test_toc_generation_no_title(self):
        self.settings['TOC']['TOC_INCLUDE_TITLE'] = 'false'
        result, expected = self._generate_toc(
                "test_data/article_with_headers.md",
                "test_data/article_with_headers_toc_no_title.html"
            )
        self.assertEqual(result.toc, expected)

    def test_toc_generation_nonascii_no_title(self):
        self.settings['TOC']['TOC_INCLUDE_TITLE'] = 'false'
        result, expected = self._generate_toc(
                "test_data/article_with_headers_nonascii.md",
                "test_data/article_with_headers_toc_nonascii_no_title.html"
            )
        self.assertEqual(result.toc, expected)

    def test_toc_generation_exclude_small_headers_no_title(self):
        self.settings['TOC']['TOC_INCLUDE_TITLE'] = 'false'
        self.settings['TOC']['TOC_HEADERS'] = '^h[1-3]'
        result, expected = self._generate_toc(
            "test_data/article_with_headers_exclude_small_headers.md",
            "test_data/article_with_headers_toc_exclude_small_headers_no_title.html"
        )
        self.assertEqual(result.toc, expected)

    def test_toc_generation_exclude_small_headers_metadata_no_title(self):
        self.settings['TOC']['TOC_INCLUDE_TITLE'] = 'false'
        result, expected = self._generate_toc(
            "test_data/article_with_headers_exclude_small_headers_metadata.md",
            "test_data/article_with_headers_toc_exclude_small_headers_no_title.html"
        )
        self.assertEqual(result.toc, expected)


    def test_bad_TOC_HEADERS(self):
        self.settings['TOC']['TOC_INCLUDE_TITLE'] = 'false'
        self.settings['TOC']['TOC_HEADERS'] = '^[1-'
        with self.assertRaises(re.error):
            self._generate_toc(
                "test_data/article_with_headers_exclude_small_headers.md",
                "test_data/article_with_headers_toc_exclude_small_headers_no_title.html"
            )

    def test_no_toc_generation(self):
        article_without_headers_path = "test_data/article_without_headers.md"
        article_without_headers = self._handle_article_generation(
            article_without_headers_path)
        toc.generate_toc(article_without_headers)
        with self.assertRaises(AttributeError):
            self.assertIsNone(article_without_headers.toc)

    def test_no_toc_generation_metadata(self):
        article_without_headers_path = "test_data/article_with_headers_metadata.md"
        article_without_headers = self._handle_article_generation(
            article_without_headers_path)
        toc.generate_toc(article_without_headers)
        with self.assertRaises(AttributeError):
            self.assertIsNone(article_without_headers.toc)
 

if __name__ == "__main__":
    unittest.main()
