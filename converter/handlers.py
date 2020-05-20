from django.conf import settings
import pdftotext
import re


def handle_upload_file(attachment):

    """Saves request.FILES attachment to MEDIA_ROOT"""

    with open(settings.MEDIA_ROOT + attachment.name, 'wb') as destination:
        for chunk in attachment.chunks():
            destination.write(chunk)


def handle_converting_pdf_to_text(attachment):

    """Opens pdf and converts to text using pdftotext library."""

    with open(settings.MEDIA_ROOT + attachment.name, "rb") as f:
        pdf = pdftotext.PDF(f)
        content_text = ''
        for page in pdf:
            content_text += page + "\n"

        # Split/Strip/Join content
        content_text = content_text.split("\n")
        content_text = [x.strip() for x in content_text if x.strip() != ""]
        content_text = "\n".join(content_text)
        content_text = re.sub(" +", ' ', content_text)

        with open(settings.MEDIA_ROOT + "converted_text.txt", 'w') as p:
            p.write(content_text)





