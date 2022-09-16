from admin_module.models import events

def allEventData(request):
    return {'eventData': events.objects.all()}