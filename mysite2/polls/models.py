from django.db import models

# Create your models here.

class Question(models.Model):
    """
    Represents a question in the application.

    This class defines the structure of a question, including its text and the
    date it was published.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime.datetime): The date and time when the question was published.

    Methods:
        __str__(): Returns a string representation of the question.

    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        """
        Return a string representation of the question.

        Returns:
            str: The text of the question.

        """
        return self.question_text

class Choice(models.Model):
    """
    Represents a choice for a question in the application.

    This class defines the structure of a choice associated with a question.
    It includes the choice text, the number of votes it has received, and the
    corresponding question.

    Attributes:
        question (Question): The question to which this choice belongs.
        choice_text (str): The text of the choice.
        votes (int): The number of votes received by the choice.

    Methods:
        __str__(): Returns a string representation of the choice.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        """
        Return a string representation of the choice.

        Returns:
            str: The text of the choice.

        """
        return self.choice_text