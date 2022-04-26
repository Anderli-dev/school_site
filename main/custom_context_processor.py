from .models import Document, DocumentFiles, Bullying, DistanceStudy, SiteTab


def subject_renderer(request):
    return {
       'documents': Document.objects.all(),
       'document_files': DocumentFiles.objects.all(),
       'Bullying': Bullying.objects.all(),
       'distance_study': DistanceStudy.objects.all(),
       'tabs': SiteTab.objects.all()
    }
