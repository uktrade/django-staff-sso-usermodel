from datetime import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_usermodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='User',
            name='sso_user_id',
            field=models.CharField(blank=False, default=str(datetime.now()), max_length=36, unique=True, verbose_name='SSO user id'),
        ),
    ]
