from celery import shared_task
from vehicle.models import Car, Moto


@shared_task
def check_milage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage

            else:
                if prev_milage < m.milage:
                    print('Неверный пробег')
                    break


@shared_task
def check_filter():
    filter_price = {'amount__lte': 5000}
    if Car.objects.filter(**filter_price).exists():
        print('Ответ по фильтру')
        # send_mail(
        #     subject="Отчёт по фильтру",
        #     message='Магины по фильтру',
        #     from_email='admin@admin.com',
        #     recipient_list=[user.email]
        # )
