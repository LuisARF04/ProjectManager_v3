import os
import pusher
from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.reminders.models import Reminder

pusher_client = pusher.Pusher(
    app_id=os.getenv('PUSHER_APP_ID'),
    key=os.getenv('PUSHER_KEY'),
    secret=os.getenv('PUSHER_SECRET'),
    cluster=os.getenv('PUSHER_CLUSTER'),
    ssl=True
)


class Command(BaseCommand):
    help = 'Revisa recordatorios pendientes y los envía a Pusher'

    def handle(self, *args, **options):
        now = timezone.now()
        pending = Reminder.objects.filter(
            reminder_at__lte=now,
            notified=False,
            task__completed=False
        )

        for r in pending:
            pusher_client.trigger(
                f'user-channel-{r.task.project.user.id}',
                'reminder-event',
                {
                    'message': f'Recordatorio: {r.task.title}',
                    'task_id': r.task.id
                }
            )

            r.notified = True
            r.save()
            self.stdout.write(f"Notificación enviada para: {r.task.title}")

        a_day_ago = now - timezone.timedelta(days=1)

        olds = Reminder.objects.filter(
            models.Q(notified=True) | models.Q(reminder_at__lte=a_day_ago)
        )

        amount_deleted = olds.count()
        olds.delete()

        if amount_deleted > 0:
            self.stdout.write(self.style.SUCCESS(
                f"Se eliminaron {amount_deleted} recordatorios viejos."))
