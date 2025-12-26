import os

def pusher_settings(request):
    return {
        'PUSHER_KEY': os.getenv('PUSHER_KEY'),
        'PUSHER_CLUSTER': os.getenv('PUSHER_CLUSTER'),
    }