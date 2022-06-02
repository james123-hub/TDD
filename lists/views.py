from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item,List

# Create your views here
def home_page(request):
    #if request.method == 'POST':
        #Item.objects.create(text=request.POST['item_text'])
        #new_item_text=request.POST['item_text']
        #return redirect('/lists/the-only-list-in-the-world/')
    
    return render(request,'home.html')
        #Item.objects.create(text=new_item_text)
    #else:
        #new_item_text=''
    
    #return render(request,'home.html',{'new_item_text': new_item_text,})
    
def view_list(request):
    items=Item.objects.all()
    return render(request,'list.html',{'items':items})
    
def new_list(request):
    list_=List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
    
    


