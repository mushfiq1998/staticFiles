from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request, 'fees/feesone.html', 
                  {'title': 'Fees Django', 'cname': 'Django', 'charge': 5000})

def fees_python(request):
    return render(request, 'fees/feestwo.html', 
                  {'title': 'Fees Python', 'cname': 'Python', 'charge': 2000})
