from django.db import models
from xml.dom import ValidationErr

def project_name_cannont_be(project_name):
    if project_name == 'all':
        raise ValidationErr(f"project name can't be {project_name}")

class ProjectDB(models.Model):
    project_name = models.CharField(max_length=50, blank=False, validators=[project_name_cannont_be])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=1500, blank=True)

    class Meta:
        db_table = 'ProjectDB'
        
    def __str__(self):
        return self.project_name
    
class TrainExpDB(models.Model):
    project = models.ForeignKey(ProjectDB, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=1500, blank=True)
    
    class Meta:
        db_table = "TrainExpDB"
        
class TrainEpochLogDB(models.Model):
    train_exp = models.ForeignKey(TrainExpDB, on_delete=models.CASCADE)
    epoch = models.IntegerField(blank=False)
    log = models.JSONField(default=dict, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TrainEpochLogDB"
        ordering = ['epoch']
    
class TrainStepLogDB(models.Model):
    train_exp = models.ForeignKey(TrainExpDB, on_delete=models.CASCADE)
    step = models.IntegerField(blank=False)
    log = models.JSONField(default=dict, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TrainStepLogDB"
        ordering = ['step']
        