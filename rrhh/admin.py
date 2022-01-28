from django.contrib import admin
from .models import interviews, jobDescription, recruitment, area
# Register your models here.

admin.site.register(interviews)
admin.site.register(area)
admin.site.register(jobDescription)
admin.site.register(recruitment)
