from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Address


@login_required
@require_POST
def add_one_address(request):
    recipient_name = request.POST['name'] 
    recipient_phone = request.POST['mobile'] 
    addr_detail = request.POST['addr'] 
    zip_code = request.POST['zip']
    try:
        addr = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        addr = Address.add_one_object(user=request.user, recipient_name=recipient_name, recipient_phone=recipient_phone, addr_detail=addr_detail, zip_code=zip_code)
    else:
        addr.recipient_phone = recipient_phone
        addr.recipient_name = recipient_name
        addr.addr_detail = addr_detail
        addr.zip_code = zip_code
        addr.save()
    next_query_str = request.GET.get('g')
    if next_query_str:
        # 从下单页面跳转过来
        return redirect('/order/commit?'+request.META['QUERY_STRING'])
    else:
        return render(request, 'user_center_site.html', {'addr':addr})


@login_required
@require_http_methods(['GET', 'POST'])
def address(request):
    if request.method == 'GET':
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            address = None
        return render(request, 'user_center_site.html', {'addr':address})
    else:
        recipient_name = request.POST['name'] 
        recipient_phone = request.POST['mobile'] 
        addr_detail = request.POST['addr'] 
        zip_code = request.POST['zip']
        try:
            addr = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            addr = Address.add_one_object(user=request.user, recipient_name=recipient_name, recipient_phone=recipient_phone, addr_detail=addr_detail, zip_code=zip_code)
        else:
            addr.recipient_phone = recipient_phone
            addr.recipient_name = recipient_name
            addr.addr_detail = addr_detail
            addr.zip_code = zip_code
            addr.save()
        next_query_str = request.GET.get('g')
        if next_query_str:
            # 从下单页面跳转过来
            return redirect('/order/commit?'+request.META['QUERY_STRING'])
        else:
            return render(request, 'user_center_site.html', {'addr':addr})