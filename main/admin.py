from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .admin_forms import *
from .models import *

admin.site.site_title = 'Адміністрування сайту НВК "Турбота"'
admin.site.site_header = 'Адміністрування сайту НВК "Турбота"'


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
