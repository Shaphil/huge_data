from django.contrib import admin

from .models import BanglaEnglishRelations, BanglaWords, EnglishWords, Senses

admin.site.register(BanglaWords)
admin.site.register(EnglishWords)
admin.site.register(Senses)
admin.site.register(BanglaEnglishRelations)
