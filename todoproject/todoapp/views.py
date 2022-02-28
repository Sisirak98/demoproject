from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todoform
from .models import tododb
from django.views.generic import ListView
from  django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class classlist(ListView):
    model = tododb
    template_name = 'home.html'
    context_object_name = 'task'

class classdetail(DetailView):
    model = tododb
    template_name = 'detailview.html'
    context_object_name = 'task'

class classup(UpdateView):
    model = tododb
    template_name = 'update.html'
    context_object_name = 'f'
    fields = ('name', 'prio', 'date')
    def get_success_url(self):
        return reverse_lazy('classdetail',kwargs={'pk':self.object.id})


class classdel(DeleteView):
    model = tododb
    template_name = 'delete.html'
    success_url = reverse_lazy('classlistview')



def home(request):
    task = tododb.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name','')
        prio=request.POST.get('prio','')
        date=request.POST.get('date','')
        m=tododb(name=name,prio=prio,date=date)
        m.save()
    return render(request, 'home.html',{'task':task})


def delete(request, tid):
    tid = tododb.objects.get(id=tid)
    if request.method == 'POST':
        tid.delete()
        return redirect('/')
    return render(request,'delete.html')


def edit(request,tid):
    t=tododb.objects.get(id=tid)
    f=todoform(request.POST or None, instance=t)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'t':t,'f':f})