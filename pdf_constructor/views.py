from django.shortcuts import render
from django import forms
from .models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .generator import save_pdf
# Create your views here.

# simple form
class SForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'profession', 'description']


def index(request):

    if request.method == 'GET':
        return render(request, "pdf_constructor/index.html", {
            'form': SForm(),
            'status': False
        })

    if request.method == 'POST':
        form = SForm(request.POST)
        data = {k:v[0] for k,v in dict(request.POST).items()}
        if form.is_valid():
            # call the generator.py function
            pdf_name, status = save_pdf(data)
            # save the data for api
            form.save()
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
        params = self.get_object(id)
        
        pdf_name, status = save_pdf(params)

        if status:
            return Response({'status': 200, 'path': f'/media/{pdf_name}.pdf'})

        return Response({'status': 400})

