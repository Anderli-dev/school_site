from .models import Document, DocumentFiles, Bullying, InfoPage


def subject_renderer(request):
    return {
        # TODO /.defer
        'documents': Document.objects.all(),
        'document_files': DocumentFiles.objects.all(),
        'Bullying': Bullying.objects.all(),
        'Pages': InfoPage.objects.all(),
    }
