from django.http import HttpResponse

def get_cookie(request):
    # Retrieve the value of the cookie named 'name'
    name_cookie = request.COOKIES.get('name', 'Cookie not set')
    return HttpResponse(f"Value of 'name' cookie: {name_cookie}")

def set_cookie(request):
    response = HttpResponse("Cookie 'name' set successfully")
    # Set a cookie named 'name' with the value 'django' and a maximum age of 15 seconds
    response.set_cookie('name', 'django', max_age=15, secure=True)
    return response

def delete_cookie(request):
    response = HttpResponse("Cookie 'name' deleted successfully")
    # Delete the cookie named 'name'
    response.delete_cookie('name')
    return response
