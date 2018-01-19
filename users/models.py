from django.db import models
from django.contrib.auth.models import User


class InviteUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None, verbose_name='Приглашение от',
                             related_name='invite_from')
    user_invite = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None,
                                    verbose_name='Пришлашение кому', related_name='invite_to')
    email = models.CharField(max_length=128, null=False, default=None, verbose_name='Email')
    url = models.CharField(max_length=128, null=False, default=None, verbose_name='Инвайт')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Отправленный инвайт'
        verbose_name_plural = 'Отправленные инвайты'

    def __str__(self):
        return "%s : %s" % (self.user.username, self.url)



