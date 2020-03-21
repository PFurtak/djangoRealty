from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        phone = request.POST['phone']
        name = request.POST['name']
        message = request.POST['message']
        user_id = request.POST['user_id']
        seller_email = request.POST['seller_email']
        
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        messages.success(request, 'Thank you, we will reach out to you shortly.')
        return redirect('/listings/'+listing_id)
