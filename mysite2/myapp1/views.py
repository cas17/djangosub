from django.shortcuts import render

# Create your views here.
def index(request):
    """
    This view handles the home-page functionality.

    :param: request (HttpRequest): The HTTP request object.
    :param: “index.html”: the file that has the desired context

    Returns:
        HttpResponse: The HTTP response for the view.
    """

    return render(request, "index.html")


def party(request):
    return render(request, 'party.html')

def leader(request):
    return render(request, 'leader.html')
