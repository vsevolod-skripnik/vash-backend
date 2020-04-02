from django.db import models
from django.utils.translation import ugettext_lazy as _

from vash.models import BaseModel


class Page(BaseModel):
    """A page on the website."""

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
    )

    content = models.TextField(
        verbose_name=_('Content'),
    )

    published_at = models.DateTimeField(
        verbose_name=_('Published at'),
        blank=True,
        null=True,
    )
