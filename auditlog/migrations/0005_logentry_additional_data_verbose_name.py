import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auditlog", "0004_logentry_detailed_object_repr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logentry",
            name="additional_data",
            field=jsonfield.fields.JSONField(
                null=True, verbose_name="additional data", blank=True
            ),
        ),
    ]
