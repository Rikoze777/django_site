from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    STATE_CHOICES = [
        ("perfomer", "Исполнитель"),
        ("customer", "Заказчик"),
    ]
    name = models.CharField("имя", max_length=100)
    address = models.CharField(
        "адрес",
        max_length=100,
        blank=True,
    )
    phonenumber = PhoneNumberField(
        "телефон",
        blank=True,
        db_index=True,
    )
    experience = models.TextField(
        "опыт",
        blank=True,
    )
    role = models.CharField(
        "роль",
        max_length=30,
        choices=STATE_CHOICES,
    )

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.name} - {self.role}"
