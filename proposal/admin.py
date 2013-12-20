'''
Created on Dec 20, 2013

@author: c3h3
'''


from django.contrib import admin
from models import ProposalModel
from forms import ProposalForm
from django.contrib.auth.models import User

class ProposalModelAdmin(admin.ModelAdmin):
    list_display = ("id","create_on","last_modified",'title', 'author', 'speech_type',
                    "language","audience_level","description","additional_info")
    
    list_filter = ('language', 'audience_level','speech_type','author')
    
    form = ProposalForm
    
    def get_queryset(self, request):
        qs = super(ProposalModelAdmin, self).get_queryset(request)
        
        if request.user in User.objects.filter(username = u"program"):
            return qs
        
        else:
            return qs.filter(author = request.user)
    
admin.site.register(ProposalModel, ProposalModelAdmin)
