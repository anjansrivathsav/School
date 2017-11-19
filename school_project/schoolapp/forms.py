from schoolapp.models import SendRequest,Post,Updates,Faculty,Gallary,Faq,Exam,Acheiver,Students,Section,Alumni,AlumniStudent
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title','text')

        widgets = {
           'title' : forms.TextInput(attrs={'class':'textinputclass'}),
           'text'  : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }

class UpdatesForm(forms.ModelForm):

    class Meta:
        model = Updates
        fields = ('title',)

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'})

        }

class FacultyForm(forms.ModelForm):

    class Meta:

        model = Faculty
        fields = ('name','areaofinterest','description','image','faculty_experience')

        widgets = {
           'title':forms.TextInput(attrs = {'calss' : 'textinputclass'})
        }



class GallaryForm(forms.ModelForm):

    class Meta:

        model = Gallary

        fields = ('video','description','image')

        widgets = {
          'description': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }



class FaqForm(forms.ModelForm):
    class Meta:

        model = Faq

        fields = ('title','answer')

        widgets = {
        'answer': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam

        fields = ('name','examdescription')

        widgets = {
        'examdescription' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        'name': forms.TextInput(attrs={'class':'textinputclass'}),
        }


class AcheiverForm(forms.ModelForm):
    class Meta:
        model = Acheiver

        fields = ('name','image','rank','ticket_no')

        widgets = {
          'name':forms.TextInput(attrs={'class':'textinputclass'})
        }


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section

        fields = ('sectionclass',)

        widgets = {
            'sectionclass':forms.TextInput(attrs={'class':'textinputclass'})
        }

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students

        fields = ('image','name','roll_no','division','attendence','quaterly_exam','half_yearly','annual','contact_no','address')



class SendRequestForm(forms.ModelForm):
    class Meta:
        model = SendRequest

        fields = ('studentname','currentclass','father_name','age','email')


class AlumniForm(forms.ModelForm):

    class Meta:
        model = Alumni
        fields = ('title','year',)


class AlumniStudentForm(forms.ModelForm):

    class Meta:
        model = AlumniStudent
        fields = ('name', 'text','image')
