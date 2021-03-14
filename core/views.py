from django.shortcuts import render
from .models import User
# Create your views here.
def homeview(request):
    return render(request,'index.html')

def transferlistview(request):
    users = User.objects.all()
    context = { 'users' : users }
    return render(request,'transfer_list.html', context)

def userView(request,name):
    users = User.objects.all()
    user = User.objects.filter(name = name).first()
    context = {
        'user':user,
        'users':users
    }
    return render(request,'user.html', context)

def confirmationView(request,name):
    recipient = request.POST.get("recipient")
    credit = request.POST.get("credit")
    sender = User.objects.filter(name = name).first()
    receiver = User.objects.filter(name = recipient).first()
    UpdatedReceiverCredit = receiver.current_credit + int(credit)
    UpdatedSenderCredit = sender.current_credit - int(credit)
    if sender.current_credit >= int(credit):
        status = True
        #update credits to database
        UpdateSender = User.objects.get(name = sender.name)
        UpdateSender.current_credit = UpdatedSenderCredit
        UpdateSender.save()

        UpdateReceiver = User.objects.get(name = receiver.name)
        UpdateReceiver.current_credit = UpdatedReceiverCredit
        UpdateReceiver.save()
    else:
        status = False
    users = User.objects.all()
    context = {
        'status': status,
        'name': name,
        'recipient': recipient,
        'credit': credit,
        'users': users
    }
    return render(request,'confirmation.html',context)