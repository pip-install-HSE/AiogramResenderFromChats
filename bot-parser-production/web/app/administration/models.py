from django.db import models


class ChatMessage(models.Model):

    sender_name = models.CharField("Sender name",  max_length=128, null=False, blank=False)
    sender_username = models.CharField("Sender username",  max_length=128, null=True, blank=True)
    
    first_digest = models.CharField("Hash 1",  max_length=32, null=False, blank=False)
    second_digest = models.CharField('Hash 2', max_length=32, null=False, blank=False)

    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Chat message'
        verbose_name_plural = 'Chat messages'

    def __str__(self):
        return str(self.sender_name) + ' ' + str(self.sender_username) + ' ' + str(self.created_at)


class Message(models.Model):
    name = models.CharField("Message id", max_length=64, null=False, unique=True)
    message = models.TextField('Message', null=False, blank=False)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.BigIntegerField("Telegram user id", primary_key=True)
    name = models.CharField("User's name", max_length=255, null=False)
    lastname = models.CharField("User's lastname", max_length=255, null=True)
    username = models.CharField("@username", max_length=32, null=True)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name


class Word(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    search_words = models.TextField('Keywords', null=True, default='')
    stop_words = models.TextField('Stopwords', null=True, default='')

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'

    def __str__(self):
        return "Search settings for " + self.user.name


class File(models.Model):
    file_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    file_id = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return self.file_name
