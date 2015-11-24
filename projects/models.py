from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Project(models.Model):
    """
    Project Model
    """
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    users = models.ManyToManyField(User)
    created_date = models.DateTimeField(default=datetime.now,
                                        blank=True)

    class Meta:
        verbose_name_plural = 'projects'


class IssueType(models.Model):
    """
    IssueType Model
    """
    name = models.CharField(max_length=200)


class IssueStatus(models.Model):
    """
    IssueStatus Model
    """
    name = models.CharField(max_length=200)


class Sprint(models.Model):
    """
    Sprint Model
    """
    project_id = models.ForeignKey(Project)
    summary = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Issue(models.Model):
    """
    Issue Model
    """
    HIGHEST = 'HE'
    HIGH = 'HI'
    MEDIUM = 'ME'
    LOW = 'LO'
    LOWEST = 'LE'
    PRIORITY_CHOICES = (
        (HIGHEST, 'Highest'),
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
        (LOWEST, 'Lowest'),
    )
    project_id = models.ForeignKey(Project)
    issue_type_id = models.ForeignKey(IssueType)
    sprint_id = models.ForeignKey(Sprint)
    summary = models.CharField(max_length=200)
    status_id = models.ForeignKey(IssueStatus)
    description = models.CharField(max_length=800)
    priority = models.CharField(max_length=2,
                                choices=PRIORITY_CHOICES,
                                default=MEDIUM)

    reporters = models.ManyToManyField(User)
    created_date = models.DateTimeField(default=datetime.now,
                                        blank=True)

    class Meta:
        verbose_name_plural = 'issues'
