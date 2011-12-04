from selenium import selenium
import os

url = os.path.expanduser("~/repo/git/scipy-2011-tutorial/build/html")

class TestCase(object):

    @classmethod
    def setup_class(cls):
        cls.sel = selenium('localhost', 4444, '*firefox', 'file://%s/' % url)
        cls.sel.start()
        cls.sel.open('index.html')
        cls.sel.wait_for_page_to_load(10000) # milliseconds

    def test_search_box_works(self):
        self.sel.type("css=input[name=q]", "abc")
        self.sel.submit("css=form.search")
        self.sel.wait_for_page_to_load(10000) # milliseconds
        assert self.sel.is_text_present("from sympy.abc import x")

    @classmethod
    def teardown_class(cls):
        cls.sel.stop()
