from django.contrib import admin
from . models import (Author,About,Skill,Fact,
                    Testimonials,Summary,Experience,
                    Education)

admin.site.register(Author)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Fact)
admin.site.register(Testimonials)
admin.site.register(Summary)
admin.site.register(Experience)
admin.site.register(Education)
