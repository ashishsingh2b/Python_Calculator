from django.shortcuts import render
import math

# Create your views here.

def calculator(request):
    c = None

    if request.method=="POST":
        if request.POST.get('num1','num2')=="":
            return render(request,"calculator.html",{'error':True})
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        opr=request.POST.get('op')
        if opr=="+":
            c=n1+n2
        elif opr=="-":
            c=n1-n2
        elif opr=="*":
            c=n1*n2
        elif opr =="/":
            c=n1/n2
        else:
            c = "invalid"

    return render(request,'calculator.html',{'c':c})

def evenodd(request):
    c=''
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,"evenodd.html",{'error':True})
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c= "Even Number"
        else:
            c="Odd Number"

    return render(request,'evenodd.html',{'c':c})

def marksheet(request):
    if request.method=="POST":
        if request.POST.get('subject1')=="" or request.POST.get('subject2')=="" or request.POST.get('subject3')=="" or request.POST.get('subject4')=="" or request.POST.get('subject5')=="" :
            return render(request,"marksheet.html",{'error':True})
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        print(t)
        p=math.floor(t*100/500)
        if p>=60:
            d="First Div"
        elif p>=48:
            d="Second DIv"
        elif p>=35:
            d="Third Div"
        else:
            d="Fail"
        

        data = {
            'total':t,
            'per':p,
            'div':d
        }
        return render(request,'marksheet.html',data)


    
    return render(request,'marksheet.html')