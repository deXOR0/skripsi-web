from django.db import models
from datetime import datetime
import uuid


class ISPU(models.Model):
    ispu_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    timestamp = models.DateTimeField(default=datetime.now)
    value = models.IntegerField()


    class Meta:
        db_table = 'ispu'

    def __repr__(self):
        return str({'ispu_id': self.ispu_id, 'timestamp': self.timestamp, 'value': self.value})

    def __str__(self):
        return str({'ispu_id': self.ispu_id, 'timestamp': self.timestamp, 'value': self.value})
