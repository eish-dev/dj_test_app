from django.db import models




class BaseDBModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True

class Books(BaseDBModel):
    book_name = models.CharField(max_length=250)
    total_copies = models.PositiveIntegerField(default=0)
    available_copies = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.book_name


class Members(BaseDBModel):
    name = models.CharField(max_length=250)


class Circulation(BaseDBModel):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


class ReservationQueue(BaseDBModel):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
