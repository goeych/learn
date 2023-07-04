from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
  if request.method == "POST":
    name = request.POST.get('full-name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    data = {
      'name':name,
      'email':email,
      'subject':subject,
      'message':message
      }

    print(data)
    receipient_email = data['email']
    print (receipient_email)

   # message = '''
   # New message:{}

    #From: {}
    #'''.format(data['message'],data['email'])
    message = f'''
    Messages: {data['message']}

    From: {data['email']}
    '''

    #send_mail(data['subject'],message,'',['goeych@gmail.com'],)
    send_mail(data['subject'],message,'',[receipient_email],)
    
  return render(request,'sendgmail/index.html')
