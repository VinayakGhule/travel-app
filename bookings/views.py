from django.shortcuts import render ,get_object_or_404, redirect
from .models import TravelPackage , Booking

def packages(request):
    packages = TravelPackage.objects.all()
    user_packages = []

    if request.user.is_authenticated:
        user_packages = Booking.objects.filter(user=request.user).values_list('package_id', flat=True)

    return render(request, 'packages.html', {
        'packages': packages,
        'user_packages': list(user_packages),  
    })
def package_detail(request, package_id):
    package = get_object_or_404(TravelPackage, pk=package_id)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return render(request, "package_detail.html", {"error": "please login to book", "package": package})
        
        travel_mode = request.POST.get('travel_mode')
        no_of_seats = int(request.POST.get('no_of_seats'))
        
        if no_of_seats > package.seats_available:
            return render(request, "package_detail.html", {
                "package": package,
                "error": "Not enough seats available."
            })
        
        total_price = no_of_seats * package.price
        
        Booking.objects.create(
            package_id=package,
            user=request.user,
            travel_mode=travel_mode,
            no_of_seats=no_of_seats,
            total_price=total_price
        )
        
        package.seats_available -= no_of_seats
        package.save()
        
        return redirect("dashboard")
    return render(request, "package_detail.html", {"package": package})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("forbidden")
    
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'bookings': bookings})