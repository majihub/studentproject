from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def details(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        phys=int(request.POST.get('physics'))
        chem=int(request.POST.get('chemistry'))
        maths=int(request.POST.get('maths'))
        cmpsc=int(request.POST.get('cmp'))
        total_marks=phys+chem+maths+cmpsc
        percent=(total_marks/400)*100
        student={
            'name':name,
            'dob':dob,
            'physics':phys,
            'chemistry':chem,
            'maths':maths,
            'computerscience':cmpsc,
            'percentage':percent
        }
        return render(request,'final.html',{'data':student})
    return render(request,'details.html')
def finalpage(request):

    return render(request,'final.html',{'name':person})