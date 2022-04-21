from django.db.models import Model, CharField, DateTimeField


class PromoCode(Model):

    code = CharField(max_length=12, blank=True, null=True, unique=True)
    group = CharField(max_length=20, null=False)

    created_at = DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"group: {self.group}, created at: {self.created_at}"
