from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.


class Post(models.Model):
    author =  models.CharField(max_length = 200)
    title  = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True,null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail",kwargs = {'pk':self.pk})

    def __str__(self):
        return self.title


class Updates(models.Model):
    title = models.CharField(max_length = 200)
    created_date = models.DateTimeField(default = timezone.now)

    def get_absolute_url(self):
        return reverse("update_list")

    def __str__(self):
        return self.title



class Faculty(models.Model):
    faculty_experience = models.IntegerField(blank = False,default = 0)
    name = models.CharField(max_length = 200)
    areaofinterest = models.CharField(max_length =200)
    description = models.TextField()
    image = models.ImageField(null = True,blank = True,height_field='height_field',width_field='width_field')
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default =0)

    def get_absolute_url(self):
        return reverse("faculty_list")

    def __str__(self):
        return self.name



class Gallary(models.Model):
    video = models.FileField(blank = True)
    description = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    image = models.ImageField(blank = True)

    def get_absolute_url(self):
        return reverse("gallary_list")



class Faq(models.Model):
    title = models.CharField(max_length = 200)
    answer = models.TextField()
    published_date = models.DateTimeField(blank = True, null = True)

    def get_absolute_url(self):
        return reverse("faq_list")

    def __str__(self):
        return self.title



class Exam(models.Model):
    name = models.CharField(max_length = 200)
    examdescription = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    def get_absolute_url(self):
        return reverse("exam_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class Acheiver(models.Model):
    exam = models.ForeignKey('schoolapp.Exam', related_name='rankers')
    name = models.CharField(max_length = 200)
    rank = models.IntegerField()
    ticket_no = models.IntegerField()
    image = models.ImageField(blank = True,null = True)


    def get_absolute_url(self):
        return reverse('acheiver_list')

    def __str__(self):
        return self.name


class Section(models.Model):
    sectionclass = models.CharField(max_length = 200)
    created_date = models.DateTimeField(default = timezone.now)

    def get_absolute_url(self):
        return reverse("section_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class Students(models.Model):
    section = models.ForeignKey('schoolapp.Section',related_name = 'students')
    image = models.ImageField(blank = True,null = True)
    name = models.CharField(max_length = 200)
    roll_no = models.IntegerField()
    division = models.CharField(max_length = 20)
    attendence = models.IntegerField()
    quaterly_exam = models.IntegerField()
    half_yearly = models.IntegerField()
    annual = models.IntegerField()
    contact_no = models.IntegerField()
    address = models.TextField()

    def get_absolute_url(self):
        return reverse("students_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


class SendRequest(models.Model):
    studentname = models.CharField(max_length = 200)
    currentclass = models.CharField(max_length = 200)
    age = models.IntegerField()
    father_name = models.CharField(max_length =200)
    email = models.CharField(max_length = 200)

    def get_absolute_url(self):
        return reverse("post_lsit")

    def __str__(self):
        return self.studentname


class Alumni(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_alumnistudent(self):
        return self.alumnistudents.filter(approved_alumnistudent=True)

    def get_absolute_url(self):
        return reverse("alumni_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title



class AlumniStudent(models.Model):
    alumni = models.ForeignKey('schoolapp.Alumni', related_name='alumnistudents')
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_alumnistudent = models.BooleanField(default=False)

    def approve(self):
        self.approved_alumnistudent = True
        self.save()

    def get_absolute_url(self):
        return reverse("alumni_list")

    def __str__(self):
        return self.text
