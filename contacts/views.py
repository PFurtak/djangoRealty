from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

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
        
        if request.user.is_authenticated:
            user_id = request.user.id 
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry on this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # #mailing
        # send_mail(
        #     'Property inquiry',
        #     'There has been an inquiry on ' + listing + '. Sign in for more details.',
        #     'dummyemail@fake.com',
        #     [seller_email, 'dummy2@gmail.com', 'admin@djangorealty.com'],
        #     fail_silently=False
        # )


        messages.success(request, 'Thank you, we will reach out to you shortly.')
        return redirect('/listings/'+listing_id)
