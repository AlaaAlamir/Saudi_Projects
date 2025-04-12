from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import FutureVision
from .forms import FutureVisionForm

# Create your views here.

def landpage(request):
        template=loader.get_template('categories.html')
        return HttpResponse(template.render())

@csrf_exempt
def vision2030(request):
        futvisi = FutureVision.objects.all()
        template=loader.get_template('vision2030.html')
        form=FutureVisionForm()
        forms={
            'form':form,
            'futvis':futvisi,
        }
        return HttpResponse(template.render(forms))

@csrf_exempt
def create(request):
    name=request.POST.get('name')
    specialization=request.POST.get('specialization')
    vision_text=request.POST.get('vision_text')
    
    FutureVis=FutureVision(name=name,specialization=specialization,vision_text=vision_text)
    FutureVis.save()
    return redirect('vision2030')

@csrf_exempt
def delete(request,id):
    vision=FutureVision.objects.get(id=id)
    vision.delete()
    return redirect('vision2030')

def edit(request,id):
    template=loader.get_template('edit.html')
    vision=FutureVision.objects.get(id=id)
    if request.method == 'POST':
        form = FutureVisionForm(request.POST, instance=vision)
        if form.is_valid():
            form.save()
            return redirect('vision2030')
    else:
        form = FutureVisionForm(instance=vision)
    items={
        'vis':vision
    }
    return render(request,'edit.html', (items))

@csrf_exempt
def update(request):
    id=request.POST.get('id')
    name=request.POST.get('name')
    specialization=request.POST.get('specialization')
    vision_text=request.POST.get('vision_text')
    
    vis=FutureVision.objects.get(id=id)
    
    vis.name=name
    vis.specialization=specialization
    vis.vision_text=vision_text
    
    vis.save()
    return redirect('vision2030')