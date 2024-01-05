from django.db import models


class PostFile(models.Model):
    title = models.CharField(max_length=100, verbose_name="File name", unique=True)
    file = models.FileField(upload_to="post_files/")
    code = models.IntegerField(default=0, verbose_name="File code", unique=True)
    download_count = models.IntegerField(default=0, verbose_name="Downloaded")

    class Meta:
        verbose_name = "Post file"
        verbose_name_plural = "Post files"

    objects = models.Manager()

    def increment_count(self):
        self.download_count += 1
        self.save()

    def __str__(self):
        return f"Title:{self.title}, code: {self.code} with {self.download_count}"

    def __repr__(self):
        return f"{self.title} | {self.file} | {self.code} | {self.download_count}"
