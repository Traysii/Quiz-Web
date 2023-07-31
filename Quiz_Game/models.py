from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Question(models.Model):
    question_text = models.CharField(max_length=300, null=True)
    op1 = models.CharField(max_length=300, null=True)    
    op2 = models.CharField(max_length=300, null=True)    
    op3 = models.CharField(max_length=300, null=True)    
    op4 = models.CharField(max_length=300, null=True)    
    ans = models.CharField(max_length=300, null=True)    

    class Meta:
        db_table= "Quiz_Game_question"