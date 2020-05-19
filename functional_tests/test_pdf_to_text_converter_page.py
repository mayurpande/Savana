import glob
import os

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
        self.assertEqual(self.browser.find_element_by_tag_name("ul").text, 'You are only allowed type of PDF.')

        # User uploads a PDF file
        self.browser.find_element_by_name('title').send_keys('Pdf file')
        self.browser.find_element_by_name('file').send_keys(PDF_FILE)
        self.browser.find_element_by_xpath("//button[@type='submit']").click()

        # File has been downloaded
        path = Path(os.environ['HOME'])
        download_folder = glob.glob(str(path / 'Downloads' / '*'))
        latest_downloaded_file = max(download_folder, key=os.path.getctime)
        self.assertIn('converted_text', latest_downloaded_file)

