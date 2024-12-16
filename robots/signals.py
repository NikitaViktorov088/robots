from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Robot

@receiver(post_save, sender=Robot)
def send_robot_availability_email(sender, instance, created, **kwargs):
    if created:
        return
    if instance.available:
        send_mail(
            subject=f"Робот {instance.model} в наличии",
            message=f"Добрый день!\n\nНедавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}. Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.customer.email],
        )
