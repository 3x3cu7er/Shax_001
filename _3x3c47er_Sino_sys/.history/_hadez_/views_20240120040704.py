from django.shortcuts import render

# Create your views here.
# system navs


def x1(request):
    return render(request, "xterminal.html")


# system navs
def x2(request):
    return render(request, "xupdate.html")


# system navs
def x3(request):
    return render(request, "xbase.html")


# system navs
def x4(request):
    return render(request, "xmain.html")


# system navs
def x5(request):
    return render(request, "sys_manage.html")


# system navs
def x6(request):
    return render(request, "root_parent.html")


# system navs
def x7(request):
    return render(request, "dash_content_overview.html")


# system navs
def x8(request):
      
    # if request.method == 'POST':
    #     uname = '*****'
    #     addr = 'account@mail.com'
    #     refnum = '**********'
    #     commentRef = request.POST.get('comID')
    #     label = request.POST.get('label')
    #     message = request.POST.get('message')
    #     newComment = comments(commentID=commentRef, label=label, details=message)
    #     newComment.save()
    
    if request.method == 'GET':
        uname = '*****'
        addr = 'account@mail.com'
        refnum = '**********'
        ref = request.GET.get('search')
        # users = userCredentials.objects.all()
        # for userAccount in users:
        #     if str(userAccount.referenceNumber) == str(ref):
        #         print('yh..')
        #         uname = userAccount.uname
        #         addr = userAccount.Address
        #         refnum = userAccount.referenceNumber
           
    return render(request, 'xlanding.html', {'uname':uname, 'addr':addr, 'refnum':refnum})


# system navs
def x9(request):
    return render(request, "xhome.html")


# system navs
def x10(request):
    return render(request, "board_confg.html")


# system navs
def x11(request):
    return render(request, "temp_access_stud.html")


# system navs
def x12(request):
    return render(request, "confg.html")


# system navs
def x13(request):
    return render(request, "xplatform.html")


# system navs
def x14(request):
    return render(request, "sys_major_home.html")

