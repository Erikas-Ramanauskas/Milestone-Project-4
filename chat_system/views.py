from django.shortcuts import render
from .models import Messages
from .forms import MessageContentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import timezone

from products.models import Product
from django.contrib.auth.models import User


@login_required
def send_message(request, product_id, user_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_superuser:
        user = User.objects.get(id=user_id)
        try:
            chat = Messages.objects.get(sender=user, product=product)
        except Messages.DoesNotExist:
            chat = Messages.objects.create(sender=user, product=product)
    else:
        try:
            chat = Messages.objects.get(sender=request.user, product=product)
        except Messages.DoesNotExist:
            chat = Messages.objects.create(
                sender=request.user, product=product)

    if request.method == 'POST':
        if request.user.is_superuser:
            message_form = MessageContentForm(
                request.POST, initial={'superuser': True})
        else:
            message_form = MessageContentForm(request.POST)

        if message_form.is_valid():
            message_content = message_form.save(commit=False)
            message_content.save()

            chat.messages.add(message_content)
            chat.timestamp = timezone.now()
            chat.save()

            # Clear the form by providing a fresh instance
            message_form = MessageContentForm()

            template = 'chat_system/message.html'
            context = {
                'message_form': message_form,
                'product': product,
                'chat': chat,
            }
            return render(request, template, context)
    else:
        message_form = MessageContentForm()

    template = 'chat_system/message.html'
    context = {
        'message_form': message_form,
        'product': product,
        'chat': chat,
    }
    return render(request, template, context)


@login_required
def messages(request):
    messages = None

    if request.user.is_superuser:
        messages = Messages.objects.all().order_by('-timestamp')
    else:
        messages = Messages.objects.filter(
            sender=request.user).order_by('-timestamp')

    template = 'chat_system/messages_list.html'
    context = {
        'messages_list': messages,
    }

    return render(request, template, context)
