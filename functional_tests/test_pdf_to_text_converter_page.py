from .base import Base
from pathlib import Path

IMAGE_FILE = str(Path("converter/static/terraza.jpg").resolve())
PDF_FILE = str(Path("converter/static/Report1.pdf").resolve())


class PdfTextConverterPageTest(Base):

    def test_when_click_link_redirects_to_pdf_converter_page(self):

        # User sees anchor link on landing page and is able to click link to move to pdf converter page
        self.browser.get(self.live_server_url + '/converter/')
        self.browser.find_element_by_link_text('PDF/TXT Converter').click()

        # User sees a form to be able to upload a PDF file to convert
        self.browser.find_element_by_tag_name('form')

        # User tries to enter upload file without any content
        self.browser.find_element_by_xpath("//button[@type='submit']").click()

        # User sees error messages saying that it is not allowed to submit an empty form
        self.browser.find_element_by_css_selector('#id_title:invalid')

        # User tries to upload a file that is not a PDF - It displays an error message saying only pdf format excepted
        self.browser.find_element_by_name('title').send_keys('Image file')
        self.browser.find_element_by_name('file').send_keys(IMAGE_FILE)
        self.browser.find_element_by_xpath("//button[@type='submit']").click()
        self.browser.find_element_by_css_selector('#id_file:invalid')


        # User uploads a PDF file - It displays a success message

        # User is redirected to a page where it shows the text