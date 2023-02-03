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

class RecentPollutant(models.Model):

    POLLUTANT_TYPE = (
        ("real", "real"),
        ("predicted", "predicted")
    )

    recent_pollutant_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    timestamp = models.DateTimeField()
    pm25 = models.FloatField()
    _type = models.CharField(db_column='type', max_length=9, choices=POLLUTANT_TYPE)

    class Meta:
        db_table = 'recent_pollutants'

    def __repr__(self):
        return str({
            'timestamp': self.timestamp,
            'pm25': self.pm25,
            'type': self._type
        })

    def __str__(self):
        return str({
            'timestamp': self.timestamp,
            'pm25': self.pm25,
            'type': self._type
        })