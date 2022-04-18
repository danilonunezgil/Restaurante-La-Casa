from distutils.text_file import TextFile
from email.mime import image
from django.db import models
from mptt.models import MPTTModel
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField
# Create your models here.

class Category(MPTTModel):
    name = models.CharField(
        verbose_name = _('Name'), 
        max_length=150, 
        help_text=_("Name of category or subcategory")
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_('Parent'),
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = [ 'tree_id', 'lft' ]
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Newsletter(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(
            verbose_name=_('Name'), 
            max_length=200, 
            help_text=_('Name of the newsletters')
        ),
        title = models.CharField(
            verbose_name=_('Title'),
            max_length=200, 
            help_text=_('Title of the  news or articles')
        ),
        abstract = models.TextField(
            verbose_name=_('Abstract'), 
            max_length=500, 
            help_text=_('Here you must write the abstract of the newsletter')
        ),
        content = RichTextField(
            verbose_name=_('content'), 
            help_text=_('Here you must write the description of the article or news.')
        )
    )
    id = models.AutoField(primary_key = True)
    category = models.ForeignKey(
        Category,
        verbose_name= _('Category'),
        on_delete= models.CASCADE,
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name = _('Image'), 
        upload_to='newsletter')
    date_created = models.DateTimeField(
        verbose_name = _('Date created'), 
        auto_now_add=True)
    date_updated = models.DateTimeField(
        verbose_name = _('Date updated'), 
        auto_now=True)
    active = models.BooleanField(
        verbose_name = _('Active'), 
        default=False, 
        help_text=_("Field to know if the newsletter is active or not active"))
    

    class Meta:
        ordering = ['pk']
        verbose_name = _('Newsletter')
        verbose_name_plural = _('Newsletters')

    def __str__(self):
        """Return title of newsletter."""
        return self.name
    
    def get_absolute_url(self):
        return reverse("news:news-detail", kwargs={'id': self.id})