from django.db import models

from core.models import BaseModel


class BookStoreModel(BaseModel):
    class Meta:
        db_table = "book_store"

    user_id = models.ForeignKey('users.UserModel', on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50)
    store_info = models.TextField()
    store_img = models.CharField(max_length=255)
    store_views = models.IntegerField(default=0)

    def __str__(self):
        return self.store_name
