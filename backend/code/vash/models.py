from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """
    Inherit all models from this model.

    Store methods and stuff common for all models.
    """

    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name=_('Updated at'),
        auto_now=True,
    )

    class Meta:
        abstract = True

    def update(self, **attributes):
        """
        Update self attributes and save.

        Use in tests to write less code.
        """
        for name in attributes:
            setattr(self, name, attributes[name])
        
        self.save()
