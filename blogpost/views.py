from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Subscriber
from .forms import SubscriberForm


# def get_context_data():
#  return{
#     'data':'some data'
#  }   

# Create your views here.
def home(request):
    
        return render(request, "blogpost/home.html")


def subscriber_list(request):
    subscribers = Subscriber.objects.all()
    return render(request, 'blogpost/subscriber_list.html', {'subscribers': subscribers})

def subscriber_detail(request, pk):
    subscriber = get_object_or_404(Subscriber, pk=pk)
    return render(request, 'blogpost/subscriber_detail.html', {'subscriber': subscriber})

def subscriber_create(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscriber_list')
    else:
        form = SubscriberForm()
    return render(request, 'blogpost/subscriber_form.html', {'form': form})

def subscriber_update(request, pk):
    subscriber = get_object_or_404(Subscriber, pk=pk)
    if request.method == 'POST':
        form = SubscriberForm(request.POST, instance=subscriber)
        if form.is_valid():
            form.save()
            return redirect('subscriber_list')
    else:
        form = SubscriberForm(instance=subscriber)
    return render(request, 'blogpost/subscriber_form.html', {'form': form})

def subscriber_delete(request, pk):
    subscriber = get_object_or_404(Subscriber, pk=pk)
    if request.method == 'POST':
        subscriber.delete()
        return redirect('subscriber_list')
    return render(request, 'blogpost/subscriber_confirm_delete.html', {'subscriber': subscriber})
