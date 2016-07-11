import unittest
from sphinx.application import Sphinx
import os


class TestConfluenceBuilder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        srcdir = os.path.join(os.getcwd(), 'testproj')
        cls.outdir = os.path.join(srcdir, 'out')
        confdir = srcdir
        doctreedir = os.path.join(srcdir, 'doctree')

        cls.app = Sphinx(srcdir, confdir, cls.outdir, doctreedir, 'confluence')
        cls.app.build(force_all=True)

    def test_registry(self):
        self.assertTrue('sphinxcontrib.confluencebuilder' in
                        self.app._extensions.keys())

    def test_heading(self):
        test_path = os.path.join(self.outdir, 'heading.conf')
        self.assertTrue(os.path.exists(test_path))

        with open(test_path, 'r') as test_file:
            lines = test_file.readlines()

            self.assertEqual(lines[0], "h1. HEADING_TEST\n")
            self.assertEqual(lines[1], '\n')
            self.assertEqual(lines[2], 'h2. SUBHEADER_TEST\n')

    def test_list(self):
        test_path = os.path.join(self.outdir, 'list.conf')
        self.assertTrue(os.path.exists(test_path))

        with open(test_path, 'r') as test_file:
            lines = test_file.readlines()
            self.assertEqual(lines[0], 'This is the beginning\n')
            self.assertEqual(lines[1], '\n')
            self.assertEqual(lines[2], "* BULLET_1\n")
            self.assertEqual(lines[3], '* BULLET_2\n')
            self.assertEqual(lines[4], '\n')
            self.assertEqual(lines[5], "# ENUMERATED_1\n")
            self.assertEqual(lines[6], '# ENUMERATED_2\n')

    def test_formatting(self):
        test_path = os.path.join(self.outdir, 'text.conf')
        self.assertTrue(os.path.exists(test_path))

        with open(test_path, 'r') as test_file:
            lines = test_file.readlines()
            self.assertEqual(lines[0], 'this is a paragraph\n')
            self.assertEqual(lines[2], '_emphasis_\n')
            self.assertEqual(lines[4], '*strong emphasis*\n')
            self.assertEqual(lines[6], '[http://website.com/]\n')

    def test_code(self):
        test_path = os.path.join(self.outdir, 'code.conf')
        self.assertTrue(os.path.exists(test_path))

        with open(test_path, 'r') as test_file:
            lines = test_file.readlines()
            self.assertEqual(lines[0], 'This is a paragraph\n')
            self.assertEqual(lines[2], '{code:title=code\n')
            self.assertEqual(lines[3], 'example|theme=FadeToGrey|linenumbers=true|language=python|firstline=0001|collapse=true}\n')
            self.assertEqual(lines[5], 'import antigravity\n')
            self.assertEqual(lines[6], 'antigravity.space(){code}\n')

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())