from .base import Base


class LandingPageTest(Base):

    """
    This is a functional test class to handle the test operations for the landing page from user's point of view.
    """

    def test_landing_page(self):

        # User goes to live server url
        self.browser.get(self.live_server_url + '/converter/')

        # There is a title
        self.assertIn('PDF/TXT Converter', self.browser.title)

        # There is a header text
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('PDF to Text Converter/Text to JSON Converter', header_text)

        # There is a paragraph text explaining
        p_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('There are two options for this site', p_text)

        # There is the option to select pdf converter or text converter in the nav bar
        nav_items = self.browser.find_elements_by_class_name('nav-item nav-link')
        for nav_item in nav_items:
            self.assertIn('TXT', nav_item.text) and self.assertIn('Convert', nav_item.text)
