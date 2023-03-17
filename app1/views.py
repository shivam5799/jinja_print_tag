from django.shortcuts import render

# Create your views here.
def jinja_print_tag(request):
    details={"name":"Dhoni",
             'age':41,
             'Gender':'Male'}

    return render(request,'jinja_print_tag.html',context=details)