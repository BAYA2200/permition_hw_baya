from django.db import models
from account.models import User


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return f'Tweet from {self.username} at {self.updated}'

    @property
    def post_username(self):
        return self.user.username


class Tweet(Post):
    text = models.CharField(max_length=140)

    def get_likes(self):
        likes = LikeTweet.objects.filter(tweet=self)
        return likes.count()

    def get_dislikes(self):
        dislikes = DislikeTweet.objects.filter(tweet=self)
        return dislikes.count()

    def __str__(self):
        return f'{self.__class__.__name__} from {self.user.username} at {self.updated}'


class Comment(Post):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def get_likes(self):
        likes = LikeTweet.objects.filter(tweet=self)
        return likes.count()

    def get_dislikes(self):
        dislikes = DislikeTweet.objects.filter(tweet=self)
        return dislikes.count()

    def __str__(self):
        return self.tweet


class LikeTweet(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'tweet']


class DislikeTweet(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'tweet']


class LikeComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'comment']


class DislikeComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'comment']
