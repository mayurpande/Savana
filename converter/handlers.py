from django.conf import settings


def handle_upload_file(attachment):

    with open(settings.MEDIA_ROOT + attachment.name, 'wb') as destination:
        for chunk in attachment.chunks():
            destination.write(chunk)


