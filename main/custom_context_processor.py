from .models import Document, DocumentFiles, Bullying, InfoPage


def subject_renderer(request):
    return {
        'documents': Document.objects.all(),
        'Bullying': Bullying.objects.exists(),
        'Pages': InfoPage.objects.only("tab", "slug", "title"),
    }
