from django.shortcuts import render
from apps.contacto.forms import ContactoFormIndex
from django.views.i18n import set_language
def home(request):
    direccion = 'home.html'
    if request.LANGUAGE_CODE == 'en':
        direccion = 'en/homeEn.html'
    
    formulario = ContactoFormIndex()
    mensaje = ''
    if request.method == "POST":
        formulario = ContactoFormIndex(request.POST)
        if formulario.is_valid():
            mensaje = "Muchas Gracias por ponerte en contacto con nosotros. Intentaremos responder lo mas antes posible"
            if request.LANGUAGE_CODE == 'en':
                mensaje = "Thank you very much for contacting us. We will try to respond as soon as possible"
    return render(request, direccion,{'form':formulario,'mensaje':mensaje})


def quienes_somos(request):
    direccion = 'quienes_somos.html'
    if request.LANGUAGE_CODE == 'en':
        direccion = 'en/quienes_somosEn.html'
    return render(request, direccion)


def set_language_view(request):
    if request.method == "POST":
        return set_language(request)
    
