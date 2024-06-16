from django.db import models

from config import settings
from users.models import User

# Create your models here.
NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    """Модель курса, параметры курса: названеие, превью, описание"""

    title = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    # upload_to - путь до папки, в которую будут сохраняться изображения
    preview_image = models.ImageField(
        upload_to="course_images", verbose_name="Превью", **NULLABLE
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец курса",
                              **NULLABLE
                              )

    def __str__(self, description=None):
        return f"{self.title}, {self.description[:50]}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель лекции, параметры лекции: название, превью, ссылка на видео-курс"""

    name = models.CharField(max_length=100, verbose_name="Название лекции")
    description = models.CharField(
        max_length=50, verbose_name="Описание лучшей лекции", **NULLABLE
    )
    preview_image = models.ImageField(
        upload_to="lesson_images", verbose_name="Превью", **NULLABLE
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", related_name="lessons",
                               **NULLABLE)
    video_link = models.URLField(verbose_name="Ссылка на видео-курс", **NULLABLE)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец лекции", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}, {self.description[:20]}"

    class Meta:
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"



class Subscription(models.Model):
    """Модель подписки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # Курс

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

class Payments(models.Model):
    """Модель платежей"""

    PAYMENT_METHODS = (
        ("cash", "Наличными"),
        ("bank", "Банковской картой"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_payment = models.DateTimeField(auto_now_add=True, verbose_name="Дата платежа")
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, **NULLABLE, verbose_name="Оплаченный Курс"
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name="Оплаченный Урок"
    )
    amount = models.PositiveIntegerField(verbose_name="Сумма платежа")
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS,
        default="bank",
        verbose_name="Способ оплаты",
    )
    session_id = models.CharField(max_length=50, verbose_name="Сессия", **NULLABLE)
    link = models.URLField(max_length=400, verbose_name="Ссылка на оплату", **NULLABLE)

    def __str__(self):
        return (
            f"{self.user} - {self.data_payment} - {self.paid_course if self.paid_course else self.paid_lesson} - "
            f"{self.amount}"
        )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ("-data_payment",)



