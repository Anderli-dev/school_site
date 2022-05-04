from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel

from .transliteration_program import slugify


class SiteTab(models.Model):
    name = models.CharField("Назва вкладки", max_length=100)

    class Meta:
        verbose_name = "Вкладка"
        verbose_name_plural = "Вкладки"

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField("Назва документа(-ів)", max_length=100)
    slug = models.SlugField("Посилання", max_length=100, unique=True)
    tab = models.ForeignKey(SiteTab,
                            on_delete=models.SET_DEFAULT,
                            verbose_name="Вкладка на якій буде знаходитися документ(-и)",
                            default="Документи")

    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Document, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('document-page', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документи'

    def __str__(self):
        return self.name


class DocumentFiles(models.Model):

    Document = models.ForeignKey(Document, default=None, on_delete=models.CASCADE)
    documents = models.FileField("PDF-файл", upload_to="files")

    objects = models.Manager()

    def __str__(self):
        return self.Document.name


class EmployeesType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employees(OrderedModel):
    name = models.CharField("Ім'я", max_length=50)
    surname = models.CharField("Прізвище", max_length=50)
    po_batkovi = models.CharField("По-батькові", max_length=50)
    type = models.ForeignKey(EmployeesType,
                             on_delete=models.SET_DEFAULT,
                             verbose_name="Розділ",
                             default=1)
    position = models.CharField(verbose_name="Посада", max_length=150)
    photo = models.ImageField("Фотографія", upload_to="employees_photo")
    about = models.TextField("Про співробітника")

    class Meta:
        verbose_name = 'Співробітника'
        verbose_name_plural = 'Співробітники'
        ordering = ("order",)

    def __str__(self):
        return self.name+" "+self.surname+" "+self.po_batkovi


class Vacancy(models.Model):
    vacancy = models.TextField("Вакансія", max_length=200)

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'

    def __str__(self):
        return self.vacancy


class Finance(models.Model):
    year = models.IntegerField("Рік")
    koshtorys = models.FileField("Кошторис", upload_to="files", blank=True, null=True)
    slug = models.SlugField(unique=True, default='')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Державне забезпечення'
        verbose_name_plural = 'Державне забезпечення'

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.year))
        super(Finance, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('finance-details', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.year)


class FinanceFiles(models.Model):

    Finance = models.ForeignKey(Finance, default=None, on_delete=models.CASCADE)

    financ_zvit = models.FileField("PDF-файл", upload_to="files", blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.Finance.year)


class BlogPsychologa(models.Model):

    title = models.CharField("Заголовок", max_length=255)
    img = models.ImageField(verbose_name="Зображення", upload_to="img")
    author = models.CharField(default="Психолог", max_length=50)
    short_post = models.TextField("Прев’ю", blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, default='')
    post = models.TextField("Текст поста")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-psychologa', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Блог психолога'

    def __str__(self):
        return self.title


class Bullying(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    img = models.ImageField(verbose_name="Зображення", upload_to="img")
    author = models.CharField(default="Адміністратор", max_length=50)
    short_post = models.TextField("Прев’ю", blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, default='')
    post = models.TextField("Текст поста")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('protidiya-bulingu', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Протидія булінгу'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    img = models.ImageField(verbose_name="Зображення", upload_to="img")
    author = models.CharField(default="Адміністратор", max_length=50)
    short_post = models.TextField("Прев’ю", blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, default='')
    post = models.TextField("Текст поста")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Новини'

    def __str__(self):
        return self.title


class InfoPage(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    post_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, default='')
    tab = models.ForeignKey(SiteTab,
                            on_delete=models.SET_DEFAULT,
                            verbose_name="Вкладка на якій буде сторінка",
                            default="Документи")
    post = models.TextField("Текст")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Сторінку'
        verbose_name_plural = 'Сторінки'

    def __str__(self):
        return self.title


class EnterSchool(models.Model):
    content = RichTextField()
    document = models.FileField("PDF-файл", upload_to="files", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk and EnterSchool.objects.exists():
            raise ValidationError('There is can be only one page')
        return super(EnterSchool, self).save(*args, **kwargs)


class DistanceLessons(OrderedModel):
    name = models.CharField("Назва", max_length=100)
    document = models.FileField("PDF-файл", upload_to="files", blank=True, null=True)

    class Meta:
        verbose_name = 'Розклад дистанційних уроків'
        verbose_name_plural = 'Розклади дистанційних уроків'
        ordering = ("order",)

    def __str__(self):
        return self.name
