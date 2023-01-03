from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    hola = _('Hola mundo')
    return render(request, 'base.html', locals())