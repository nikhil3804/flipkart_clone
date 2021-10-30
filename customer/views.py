from django.shortcuts import render,redirect
from django import forms
from .forms import f1,f2
from .models import d1,d2
from django.contrib.auth.models import User



#def home(request):
##### return render(request,'home.html')


def show(request):
    sp=User.objects.all()
    print(sp)
    return render(request,'show.html',{'show':sp})





def register(request):

    formz=f1((request.POST))
    if(request.method=='POST'):
        if formz.is_valid():
            username=formz.cleaned_data['username']
            password=formz.cleaned_data['password']
            #address=formz.cleaned_data['address']
            user = User.objects.create_user(username,password)
            
            return redirect('/accounts/login')

        else:
            return render(request,'register.html',{'errors':formz.errors})
    else:
        return render(request,'register.html',{'show':formz})



def update(request,id):
    sk=d2.objects.get(id=id)
    formz=f2(request.POST)
    if formz.is_valid():
        sk.Address=formz.cleaned_data['Address']
        sk.Street_name=formz.cleaned_data['Street_name']
        sk.Near_location=formz.cleaned_data['Near_location']
        sk.save()
        print("form submitted")
        return redirect('/register/addresses')
    
    else:
        print('form not submitted',f1.errors)
    return render(request,'edit.html',{'data':sk})
    


    
    



def edit(request,id):
    s2=d2.objects.get(id=id)
    return render(request,'edit.html',{'s2':s2})
        








def no(request):
    formz=f2((request.POST))
    if(request.method=='POST'):
        if formz.is_valid():
            Address=formz.cleaned_data['Address']
            Street_name=formz.cleaned_data['Street_name']
            Near_location=formz.cleaned_data['Near_location']
            
            
            db=d2(Address=Address,Street_name=Street_name,Near_location=Near_location)
            db.save()
            return redirect('/register/no')
        else:
            return render(request,'no.html',{'error1':formz.errors})
    else:
        return render(request,'no.html',{'open':f2})

 

def slides(request):
    formz=f2((request.POST))
    if(request.method=='POST'):
        if formz.is_valid():
            Address=formz.cleaned_data['Address']
            Street_name=formz.cleaned_data['Street_name']
            Near_location=formz.cleaned_data['Near_location']
          
            
            
            db=d2(Address=Address,Street_name=Street_name,Near_location=Near_location)
            db.save()
            return redirect('/register/no')
        else:
            return render(request,'slides.html',{'error1':formz.errors})
    else:
        return render(request,'slides.html',{'open':f2})



def lappy(request):
    formz=f2((request.POST))
    if(request.method=='POST'):
        if formz.is_valid():
            Address=formz.cleaned_data['Address']
            Street_name=formz.cleaned_data['Street_name']
            Near_location=formz.cleaned_data['Near_location']
            
            
            db=d2(Address=Address,Street_name=Street_name,Near_location=Near_location)
            db.save()
            return redirect('/register/lappy')
        else:
            return render(request,'lappy.html.html',{'error1':formz.errors})
    else:
        return render(request,'lappy.html',{'open':f2})
            
def addresses(request):
    add=d2.objects.all()
    return render(request,'addresses.html',{'show1':add})



def cart(request):
    sk=d2.objects.all()
    return render(request,'cart.html',{'cart':cart})

def delete(request,id):

    sps=d2.objects.get(id=id)
    sps.delete()
    return redirect('/register/addresses')




            


    





# Create your views here.



