from datetime import datetime

from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone
from .views import index
from .models import CloudServiceProvider


class ServiceModelTests(TestCase):

    def test_model_created_time(self: TestCase) -> None:
        """
        测试CloudServiceProvider的created是否正常记录创建时间
        
        Returns:
            None
        """
        time: datetime = timezone.now()
        future_question: CloudServiceProvider = CloudServiceProvider()
        future_question.save()
        self.assertIs(
            time - datetime.timedelta(seconds=10) < future_question.created < time + datetime.timedelta(seconds=10),
            True)
