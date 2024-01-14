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
    superuser = False

    if request.user.is_superuser:
        regular_user = User.objects.get(id=user_id)
        superuser = True
        try:
            chat = Messages.objects.get(sender=regular_user, product=product)
            chat.superuser_read = True
            chat.save()
        except Messages.DoesNotExist:
            chat = Messages.objects.create(
                sender=regular_user, product=product)
    else:
        regular_user = request.user
        try:
            chat = Messages.objects.get(sender=request.user, product=product)
            chat.user_read = True
            chat.save()
        except Messages.DoesNotExist:
            chat = Messages.objects.create(
                sender=request.user, product=product)

    if request.method == 'POST':
        message_form = MessageContentForm(request.POST)

        if message_form.is_valid():
            message_content = message_form.save(commit=False)
            message_content.superuser = request.user.is_superuser
            message_content.save()

            chat.messages.add(message_content)
            chat.timestamp = timezone.now()

            chat.last_message = message_content.content
            chat.last_message_superuser = superuser

            # Update read status based on the sender
            if request.user.is_superuser:
                chat.user_read = False
            else:
                chat.superuser_read = False

            chat.save()

            # Clear the form by providing a fresh instance
            message_form = MessageContentForm()

            template = 'chat_system/message.html'
            context = {
                'message_form': message_form,
                'product': product,
                'chat': chat,
                'customer': regular_user,
            }
            return render(request, template, context)
    else:
        message_form = MessageContentForm()

    template = 'chat_system/message.html'
    context = {
        'message_form': message_form,
        'product': product,
        'chat': chat,
        'customer': regular_user,
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
