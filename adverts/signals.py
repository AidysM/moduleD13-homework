from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_managers, mail_admins, send_mail
from .models import Reply


# создаём функцию обработчик с параметрами под регистрацию сигнала
# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и
# в отправители надо передать также модель
@receiver(post_save, sender=Reply)
def notify_managers_post(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.text} {instance.created_reply.strftime("%d %m %Y")}'
    else:
        subject = f'Reply changed for {instance.text} {instance.created_reply.strftime("%d %m %Y")}'

    # mail_managers(
    #     subject=subject,
    #     message=instance.text,
    # )

    send_mail(
        subject=subject,
        message=instance.text,
        from_email='mongushit@yandex.ru',
        recipient_list=[instance.user.email, instance.advert.announcer.user.email, ]
    )


@receiver(post_delete, sender=Reply)
def notify_managers_post_canceled(sender, instance, **kwargs):
    subject = f'{instance.text} has canceled his reply!'

    # mail_managers(
    #     subject=subject,
    #     message=f'Canceled reply for {instance.created_reply.strftime("%d %m %Y")}',
    # )

    print(subject)

