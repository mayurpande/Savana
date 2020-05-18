from .base import Base


class PdfTextConverterPageTest(Base):

    def test_when_click_link_redirects_to_pdf_converter_page(self):

        # User sees anchor link on landing page and is able to click link to move to pdf converter page
        self.browser.get(self.live_server_url + '/converter/')
        self.browser.find_element_by_link_text('PDF/TXT Converter').click()

        # User sees a form to be able to upload a PDF file to convert

        # User tries to upload a file that is not a PDF - It displays an error message saying only pdf format excepted

        # User uploads a PDF file - It displays a success message

        # User is redirected to a page where it shows the text