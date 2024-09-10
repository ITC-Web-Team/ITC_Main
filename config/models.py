from django.db import models

#----------- Clubs, Tech Team and Other Bodies
class Body(models.Model):
  name = models.CharField(max_length=100)
  type = models.IntegerField(choices=[(0, 'Clubs'), (1, 'Tech Team'), (2, 'Other Bodies')])
  short_description = models.CharField(max_length=100)
  description = models.TextField()
  contact_email = models.EmailField()
  instagram = models.URLField(blank=True, null=True)
  facebook = models.URLField(blank=True, null=True)
  github = models.URLField(blank=True, null=True)
  linkedin = models.URLField(blank=True, null=True)
  website = models.URLField(blank=True, null=True)
  logo = models.ImageField(upload_to='logos/', blank=True, default='logos/default_logo.png')

  def __str__(self):
    return self.name

class Member(models.Model):
  body = models.ForeignKey('Body', on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  priority = models.IntegerField(default=0)
  image = models.ImageField(upload_to='members/', blank=True)

  def __str__(self):
    return self.name + ' - ' + self.position
  
#----------- Achievements 
class Achievement (models.Model):
  body = models.ForeignKey('Body', on_delete=models.CASCADE)
  date = models.DateField()
  title = models.CharField(max_length=100)
  description = models.TextField()

  def __str__(self):
    return self.title


#----------- Portals and TechStacks
class Portal(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  link = models.URLField()
  banner = models.ImageField(upload_to='banners/', blank=True)
  techstacks = models.ManyToManyField('TechStack')

  def __str__(self):
    return self.name
  
class TechStack(models.Model):
  name = models.CharField(max_length=100)
  logo = models.ImageField(upload_to='techstack/', blank=True)

  def __str__(self):
    return self.name
  
# -------- cabinet and contacts
class Cabinet(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)
    image = models.ImageField(upload_to='cabinet/', blank=True)
    email = models.EmailField(blank=True, null=True)  
    phone = models.CharField(max_length=15, blank=True, null=True)  
    linkedin = models.URLField(blank=True, null=True) 
    instagram = models.URLField(blank=True, null=True)  
    facebook = models.URLField(blank=True, null=True)  

    def __str__(self):
        return f'{self.name} - {self.position}'


#-----------  WorkReports

class WorkReport(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to='workreports/')
  url = models.URLField()

  def __str__(self):
    return self.title
  

#-----------  Hall of Fame

class InterIIT(models.Model):
  logo = models.ImageField(upload_to='interiit/')
  title = models.CharField(max_length=100)
  description = models.TextField()
  img = models.ImageField(upload_to='interiit/')
  gold = models.IntegerField(default=0)
  silver = models.IntegerField(default=0)
  bronze = models.IntegerField(default=0)  

  def __str__(self):
    return self.year + ' - ' + self.location + ' - ' + self.position
  

class ProblemStatements(models.Model):
  interiit = models.ForeignKey('InterIIT', on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.TextField()
  position = models.IntegerField(default=0)
  img = models.ImageField(upload_to='problemstatements/')
  link = models.URLField()

  def __str__(self):
    return self.title
  

class Gallery(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to='gallery/')

  def __str__(self):
    return self.title