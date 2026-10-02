from decimal import Decimal, ROUND_HALF_UP
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


class Flan(models.Model):
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="flanes/", blank=True, null=True)
    destacado = models.BooleanField(default=False)
    descuento_inscrito = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Porcentaje de descuento para clientes registrados (0 a 100)",
    )

    class Meta:
        verbose_name = "Flan"
        verbose_name_plural = "Flanes"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    @property
    def precio_registrado(self):
        factor = (Decimal("100") - self.descuento_inscrito) / Decimal("100")
        precio = Decimal(self.precio) * factor
        return int(precio.quantize(Decimal("1"), rounding=ROUND_HALF_UP))

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.nombre)
            slug, n = base, 2
            while Flan.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)