from .base import Base
from pathlib import Path

import os
import glob

IMAGE_FILE = str(Path("converter/static/terraza.jpg").resolve())
TXT_FILE = str(Path("converter/static/converted_text.txt").resolve())


class TxtToJsonConverter(Base):

    def test_user_uploads_txt_file_and_gets_json_output(self):

        # User sees anchor link on landing page and is able to click link to move to pdf converter page
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('TXT/JSON Converter').click()

        # User sees a form to be able to upload a PDF file to convert
        self.browser.find_element_by_tag_name('form')

        # User tries to enter upload file without any content
        self.browser.find_element_by_xpath("//button[@type='submit']").click()

        # User sees error messages saying that it is not allowed to submit an empty form
        self.browser.find_element_by_css_selector('#id_file:invalid')

        # User tries to upload a file that is not a TXT - It displays an error message saying only TXT format excepted
        self.browser.find_element_by_name('file').send_keys(IMAGE_FILE)
        self.browser.find_element_by_xpath("//button[@type='submit']").click()
        self.assertEqual(self.browser.find_element_by_tag_name("ul").text, 'You are only allowed type of TXT.')

        # User uploads a TXF file
        self.browser.find_element_by_name('file').send_keys(TXT_FILE)
        self.browser.find_element_by_xpath("//button[@type='submit']").click()
        # TODO Assert message
        self.browser.find_element_by_name('flash message')

        # File has been downloaded
        path = Path(os.environ['HOME'])
        download_folder = glob.glob(str(path / 'Downloads' / '*'))
        latest_downloaded_file = max(download_folder, key=os.path.getctime)
        self.assertIn('converted_text', latest_downloaded_file)
