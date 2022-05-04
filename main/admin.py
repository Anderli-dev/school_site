from django.contrib import admin
from django.urls import path
from ordered_model.admin import OrderedModelAdmin

from .admin_forms import *
from .models import *
from .views import EnterPageView

admin.site.site_title = 'Адміністрування сайту НВК "Турбота"'
admin.site.site_header = 'Адміністрування сайту НВК "Турбота"'


_admin_site_get_urls = admin.site.get_urls


def get_urls():
    urls = _admin_site_get_urls()
    urls += [
            path('main/join-document', admin.site.admin_view(EnterPageView.as_view()), name="enter-page"),
        ]
    return urls


admin.site.get_urls = get_urls
# admin.autodiscover()
# admin.site.enable_nav_sidebar = True


class DocumentFilesAdmin(admin.StackedInline):
    model = DocumentFiles
    verbose_name = "Документ"
    verbose_name_plural = "Документи"
    extra = 0
    min_num = 1


@admin.register(Document)
class DocumentAdmin(OrderedModelAdmin):
    inlines = [DocumentFilesAdmin]
    exclude = ["slug"]


@admin.register(Employees)
class EmployeesAdmin(OrderedModelAdmin):
    list_display = ('surname', 'name', 'move_up_down_links')
    form = EmployeesAdminForm


class FinanceFilesAdmin(admin.StackedInline):
    model = FinanceFiles
    verbose_name = "Документ що до придбаних товарів, виконаних робіт, послуг за рахунок загального бюджету"
    verbose_name_plural = "Документи"
    extra = 0
    min_num = 1


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    inlines = [FinanceFilesAdmin]
    exclude = ["slug"]


@admin.register(BlogPsychologa)
class BlogPsychologaAdmin(admin.ModelAdmin):
    form = BlogPsychologaAdminForm
    exclude = ["slug", "author"]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    exclude = ["slug", "author"]


@admin.register(Bullying)
class BullyingAdmin(admin.ModelAdmin):
    form = BullyingForm
    exclude = ["slug", "author"]


admin.site.register(Vacancy)


@admin.register(InfoPage)
class BullyingAdmin(admin.ModelAdmin):
    form = InfoPageForm
    exclude = ["slug"]


@admin.register(DistanceLessons)
class DistanceLessons(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')
