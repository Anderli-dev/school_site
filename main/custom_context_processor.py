from .models import Document, Bullying, InfoPage, DistanceLessons


def subject_renderer(request):
    return {
        'documents': Document.objects.all(),
        'Bullying': Bullying.objects.exists(),
        'DistancePages': InfoPage.objects.filter(tab=3).exists(),
        'DistanceDocuments': Document.objects.filter(tab=3).exists(),
        'DistanceLessons': DistanceLessons.objects.exists(),
        'Pages': InfoPage.objects.only("tab", "slug", "title"),
    }
