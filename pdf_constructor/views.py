from django.shortcuts import render
from django import forms
from .models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .generator import save_pdf
# Create your views here.

# simple form
class SForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)
    profession = forms.CharField(label='profession', max_length=50)
    description = forms.CharField(label='description', max_length=100)


def index(request):

    if request.method == 'GET':
        return render(request, "pdf_constructor/index.html", {
            'form': SForm(),
            'status': False
        })

    if request.method == 'POST':
        form = SForm(request.POST)
        data = {k:v[0] for k,v in dict(request.POST).items()}
        print(data)
        if form.is_valid():
            
            pdf_name, status = save_pdf(data)
            
            return render(request, "pdf_constructor/index.html", {
                    'form': SForm(),
                    'status': status,
                    'path': f'/media/{pdf_name}.pdf'
                })


class generatePdf(APIView):

    def get_object(self, id):
        try:
            obj = Profile.objects.get(id=id)
        except obj.DoesNotExist:
            return Response ({'status': 400})
    
    def get(self, request, id):
        params = get_object(id)
        
        pdf_name, status = save_pdf(params)

        if status:
            return Response({'status': 200, 'path': f'/media/{pdf_name}.pdf'})

        return Response({'status': 400})

