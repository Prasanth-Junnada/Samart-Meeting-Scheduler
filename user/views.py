from django.shortcuts import render,redirect
from user.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LogoutView


def availability(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User1.objects.get(user_id=user_id)
                
                user_avail, created = avail.objects.get_or_create(user=user)

             
                user_avail.sun = request.POST.get('sun')
                user_avail.mon = request.POST.get('mon')
                user_avail.tue = request.POST.get('tue')
                user_avail.wed = request.POST.get('wed')
                user_avail.thr = request.POST.get('thr')
                user_avail.fri = request.POST.get('fri')
                user_avail.sat = request.POST.get('sat')

               
                user_avail.sun_start = request.POST.get('sust')
                user_avail.sun_end = request.POST.get('suet')
                user_avail.mon_start = request.POST.get('mst')
                user_avail.mon_end = request.POST.get('met')
                user_avail.tue_start = request.POST.get('tust')
                user_avail.tue_end = request.POST.get('tuet')
                user_avail.wed_start = request.POST.get('wst')
                user_avail.wed_end = request.POST.get('wet')
                user_avail.thu_start = request.POST.get('thst')
                user_avail.thu_end = request.POST.get('thet')
                user_avail.fri_start = request.POST.get('frst')
                user_avail.fri_end = request.POST.get('fret')
                user_avail.sat_start = request.POST.get('sast')
                user_avail.sat_end = request.POST.get('saet')

                user_avail.save()
                messages.success(request, 'Availability updated successfully')
                return redirect('availability')  
            except User1.DoesNotExist:
                messages.error(request, 'User not found')
                print("User not found") 
        else:
            messages.error(request, 'User not logged in')
            print("User not logged in") 
    return render(request, 'availability.html')




def meet(request):
    user_id = request.session.get('user_id')
    user = User1.objects.get(pk=user_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        link = request.POST.get('link')
        email = request.POST.get('email')
        duration = request.POST.get('duration')
        desc = request.POST.get('desc')

        emails = [e.strip() for e in email.split(',')]
        non_existent_emails = []

        for email in emails:
            try:
                user_obj = User1.objects.get(email=email)
                mail_message = f'Event Name: {name}\n Location: {location} \n You can join this meeting from your computer, tablet, or smartphone. \n Meet Link: {link} \n Phone Number: +91 85558 87986 \n Company Name: Codebook \n Please share anything that will help prepare for our meeting. I am looking for your service. \n powered by: Codebook.in'

                # Send email
                send_mail('Meet link', mail_message, settings.EMAIL_HOST_USER, [email], fail_silently=False)

                meeting = Meeting.objects.create(
                    creator_user_id=user_id,
                    user=user_obj,
                    link=link,
                    name=name,
                    duration=duration,
                    location=location,
                    desc=desc,
                    mail=email
                )
            except User1.DoesNotExist:
                non_existent_emails.append(email)

        if non_existent_emails:
            messages.error(request, f"The following email(s) do not exist in the database: {', '.join(non_existent_emails)}")
        if len(emails) != len(non_existent_emails):  # Check if there are any successful creations
            messages.success(request, "Meetings created successfully!")

    return redirect('dashboard')



def contact(request):
    template_name = 'contact.html'
    return render(request,template_name)

from django.contrib.auth.decorators import login_required




def features(request):
    template_name = 'features.html'
    return render(request,template_name)

def index(request):
    template_name = 'index.html'
    return render(request,template_name)

def integrations(request):
    template_name = 'integrations.html'
    return render(request,template_name)

import random
def user_login(request):
    template_name = 'login.html'
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User1.objects.get(email=email, password=password)
            if user.verify == 'verified':
                request.session['user_id'] = user.user_id
                messages.success(request, 'Login successful')
                return redirect('dashboard')
            elif user.verify == 'no':
                id = user.user_id
                return redirect('otp', id=id)
            else:
                messages.error(request, 'Account not verified yet. Check your email for OTP.')
        except User1.DoesNotExist:
            messages.error(request, 'Login failed. Please check your email and password.')

    return render(request, template_name)






def otp(request, id):
    template_name = 'otp.html'
    user = User1.objects.get(pk=id)
    if request.method == 'POST':
        otpn = request.POST.get('otp')
        otpn = int(otpn)
        if otpn == user.otp:
            user.verify = 'verified'
            user.save()
            messages.success(request, 'Login successful')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    return render(request, template_name)



def dashboard(request):
    user_id = request.session.get('user_id')
    user = User1.objects.get(user_id=user_id)
    user_email = user.email

    user_meetings = Meeting.objects.filter(creator_user_id=user_id)

    meetings_for_user = Meeting.objects.filter(mail=user_email)

    context = {
        'user_meetings': user_meetings,
        'meetings_for_user': meetings_for_user,
        
    }

    return render(request, 'dashboard.html', context)


def new_meeting(request):
    template_name = 'new-meeting.html'
    return render(request,template_name)



from django.contrib import messages
def one_to_one(request):
    user_id = request.session.get('user_id')
   
    if request.method == 'POST':
        email = request.POST.get('email')
        entered_day = request.POST.get('day') 

        try:
            user = User1.objects.get(email=email)
            user_avail = avail.objects.filter(user=user).first()

            if user_avail:
                day_attr = entered_day[:3].lower()
                if getattr(user_avail, day_attr, False):
                    print(f"User Email: {user.email}")
                    print(f"Full Name: {user.fullname}")
                    print(f"Availability on {entered_day}: Available")
                    meeting = Meeting.objects.create(
                        creator_user_id=user_id,
                        name=request.POST.get('name'),
                        location=request.POST.get('location'),
                        link=request.POST.get('link'),
                        user=user,
                        desc=request.POST.get('desc'),
                        mail=request.POST.get('email'),
                        duration=request.POST.get('duration'),
                        time=request.POST.get('time'),
                        day=entered_day
                    )

                    meeting.save()
                    message = "Meeting is Created!"
                    messages.success(request, message)
                    return redirect("one_to_one")
                else:
                    message = f"{user.fullname} is not available on {entered_day}."
                    messages.info(request, message)
                    return render(request, 'one-ot-one.html')
            else:
                error_message = "User's availability data not found."
                messages.error(request, error_message) 
                return render(request, 'one-ot-one.html', {'error_message': error_message})
        except User1.DoesNotExist:
            error_message = "User with the provided email not found."
            messages.error(request, error_message) 
            return render(request, 'one-ot-one.html', {'error_message': error_message})

    return render(request, 'one-ot-one.html')






def group_meetings(request):
    template_name = 'group-meetings.html'
    return render(request,template_name)

def collective(request):
    template_name = 'collective.html'
    return render(request,template_name)

def round_robin(request):
    template_name = 'round-robin.html'
    return render(request,template_name)

import urllib.request
import urllib.parse
def sendSMS(user, otp, mobile):
    data = urllib.parse.urlencode({
        'username': 'Codebook',
        'apikey': '56dbbdc9cea86b276f6c',
        'mobile': mobile,
        'message': f'Hello {user}, your OTP for account activation is {otp}. This message is generated from https://www.codebook.in server. Thank you',
        'senderid': 'CODEBK'
    })
    data = data.encode('utf-8')
    request = urllib.request.Request("https://smslogin.co/v3/api.php?")
    f = urllib.request.urlopen(request, data)
    return f.read()

def sign_up(request):
    template_name = 'sign-up.html'
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        print("Full name: ",fullname,"Email:", email,'Password:',password )
        gen_otp = random.randint(0000, 9999)
        print(gen_otp)
        response = sendSMS(fullname, gen_otp, mobile)

        # Handle the response as needed
        print(response)
        User1.objects.create(email = email,fullname = fullname,password = password, mobile=mobile, otp=gen_otp)
        messages.success(request, 'Registration successfulll')
    return render(request,template_name)


def profile(request):
    template_name = 'profile.html'
    user =  request.session['user_id']
    user_meetings = Meeting.objects.filter(creator_user_id=user)
    user_meetings_count = user_meetings.count()


    user = User1.objects.get(user_id = user)
    user_email = user.email
    

    meetings_for_user = Meeting.objects.filter(mail=user_email)
    meetings_for_user_count = meetings_for_user.count()
 
    total_meeting_count = meetings_for_user_count + user_meetings_count

    if request.method == 'POST':
        name= request.POST.get('name')
        email = request.POST.get('email')
        password   = request.POST.get('password')
        user.fullname = name
        user.email = email
        user.password = password
        user.save()
        messages.success(request, 'Changes updated successfull')
    context = {'i':user,
               'user_meetings_count':user_meetings_count,
                'meetings_for_user_count':meetings_for_user_count,
                'total_meeting_count':total_meeting_count
               }

    return render(request,template_name,context)