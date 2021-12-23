from django.shortcuts import render

# Create your views here.
def homepage(request):
    """
    A view to generate the websites homepage or index
    """

    template = 'website/homepage.html'

    return render(request, template)


def budgeting(request):
    """
    A view to generate the budgeting page on the website
    """

    template = 'website/budgeting.html'

    return render(request, template)