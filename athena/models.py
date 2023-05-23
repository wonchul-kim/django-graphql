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
    
class SubProjectDB(models.Model):
    project = models.ForeignKey(ProjectDB, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50, blank=False)
    sub_project_name = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=1500, blank=True)

    class Meta:
        db_table = 'SubProjectDB'
        
    def __str__(self):
        return self.sub_project_name    
    
class TrainExpDB(models.Model):
    sub_project = models.ForeignKey(SubProjectDB, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50, blank=False)
    sub_project_name = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1500, blank=True)
    
    class Meta:
        db_table = "TrainExpDB"
        ordering = ['sub_project']
        
class TrainExpServerInfoDB(models.Model):
    train_exp = models.ForeignKey(TrainExpDB, on_delete=models.CASCADE)
    server_host_name = models.CharField(max_length=20, blank=True)
    container_name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=1500, blank=True)

    class Meta:
        db_table = "TrainExpServerInfoDB"
        ordering = ['train_exp']
        
class TrainExpTrainInfoDB(models.Model):
    train_exp = models.ForeignKey(TrainExpDB, on_delete=models.CASCADE)
    parameters = models.JSONField(default=dict, blank=True)
    configurations = models.JSONField(default=dict, blank=True)
    options = models.JSONField(default=dict, blank=True)
    description = models.CharField(max_length=1500, blank=True)

    task = models.CharField(max_length=15, blank=True)
    model_name = models.CharField(max_length=30, blank=True)
    last_epoch = models.IntegerField(blank=True)
    resume = models.BooleanField(blank=True)
    
    
    class Meta:
        db_table = "TrainExpTrainInfoDB"
        ordering = ['train_exp']
        
class TrainEpochTrainLogDB(models.Model):
    '''
        mode: one of train, val, and test
    '''
    train_exp = models.ForeignKey(TrainExpDB, on_delete=models.CASCADE)
    epoch = models.IntegerField(blank=False)
    log = models.JSONField(default=dict, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TrainEpochTrainLogDB"
        ordering = ['epoch']

class TrainEpochSystemDB(models.Model):
    '''
        mode: one of train, val, and test
    '''
    train_exp = models.ForeignKey(TrainExpDB, on_delete=models.CASCADE)
    epoch = models.IntegerField(blank=False)
    system = models.JSONField(default=dict, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TrainEpochSystemDB"
        ordering = ['epoch']
            
class TrainEpochValLogDB(models.Model):
    '''
        mode: one of train, val, and test
    '''
    train_exp = models.ForeignKey(TrainExpDB, on_delete=models.CASCADE)
    epoch = models.IntegerField(blank=False)
    log = models.JSONField(default=dict, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TrainEpochValLogDB"
        ordering = ['epoch']
    
class TrainStepTrainLogDB(models.Model):
    '''
        mode: one of train, val, and test
    '''
    train_exp = models.ForeignKey(TrainExpDB, on_delete=models.CASCADE)
    step = models.IntegerField(blank=False)
    log = models.JSONField(default=dict, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TrainStepTrainLogDB"
        ordering = ['step']
        
class TrainStepValLogDB(models.Model):
    '''
        mode: one of train, val, and test
    '''
    train_exp = models.ForeignKey(TrainExpDB, on_delete=models.CASCADE)
    step = models.IntegerField(blank=False)
    log = models.JSONField(default=dict, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TrainStepValLogDB"
        ordering = ['step']