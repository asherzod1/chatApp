from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f'{self.user.first_name} {self.user.last_name}'
        elif self.user.first_name:
            return f'{self.user.first_name}'
        elif self.user.last_name:
            return f'{self.user.last_name}'
        else:
            return self.user.username

class Group(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Person, related_name='cretaed_groups', on_delete=models.CASCADE)
    def setcomment(self, comment, person):
        new_comment = Comment.objects.create(
            group=self,
            comment=comment,
            person=person,
        )
    def __str__(self):
        return self.name

class Comment(models.Model):
    group = models.ForeignKey(Group, related_name='comments', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    def __str__(self):
        return f"{self.person}'s comment is {self.comment}"