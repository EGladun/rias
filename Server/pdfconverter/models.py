from django.db import models


class File(models.Model):
  file1 = models.FileField(blank=False, null=False)
  file2 = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)


class Fileupload(models.Model):
  file = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)
