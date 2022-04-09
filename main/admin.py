from django.contrib import admin
from . models import Author,About,Skill,Fact,Testimonials

admin.site.register(Author)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Fact)
admin.site.register(Testimonials)
