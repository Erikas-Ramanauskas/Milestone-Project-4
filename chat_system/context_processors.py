from .models import Messages


def unread_messages_count(request):
    unread_count = 0

    if request.user.is_authenticated:
        if request.user.is_superuser:
            unread_count = Messages.objects.filter(
                superuser_read=False).count()
        else:
            unread_count = Messages.objects.filter(
                sender=request.user, user_read=False).count()

    return {'unread_messages_count': unread_count}
