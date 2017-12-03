from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from schoolapp.forms import SendRequestForm,PostForm,UpdatesForm,FacultyForm,GallaryForm,FaqForm,ExamForm,AcheiverForm,StudentsForm,SectionForm,AlumniForm,AlumniStudentForm
from schoolapp.models import Post,Updates,Faculty,Gallary,Faq,Exam,Acheiver,Students,Section,Alumni,AlumniStudent
from django.utils import timezone
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from  django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMessage
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(),content_type='text/plain')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404



class InfrastructureView(TemplateView):
    template_name = 'infrastructure.html'

class ContactView(TemplateView):
    template_name = 'contactus.html'

class EventView(TemplateView):
    template_name = 'events.html'


class ActivityView(TemplateView):
    template_name = 'activities.html'

class AboutView(TemplateView):
    template_name = 'index.html'

class AboutmeView(TemplateView):
    template_name = 'aboutme.html'

class AdmissionView(TemplateView):
    template_name = 'admissions.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class CareerView(TemplateView):
    template_name = 'careers.html'

class AcheivementView(TemplateView):
    template_name = 'acheivements.html'

class StudentLifeView(TemplateView):
    template_name = 'studentslife.html'

def send_verification(email,msg):
    print("send verification")
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.set_debuglevel(1)
        server.starttls()
        server.ehlo()
        server.login('anjansrivathsav1997@gmail.com','30anjan97')
        server.sendmail('anjansrivathsav1997@gmail.com',email,msg)
        server.quit()
        print('successfully sent the mail')
    except:
        print("failed to sent")


def verify(request):
    message = render_to_string('schoolapp/sending.html')
    send_verification('shobhitpandey8@gmail.com',message)
    return redirect('index')

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte  = timezone.now()).order_by('-published_date')

class FacultyListView(ListView):
    model = Faculty

    def get_queryset(self):
        return Faculty.objects.order_by('-faculty_experience')


class UpdatesListView(ListView):
    model = Updates

    def get_queryset(self):
        return Updates.objects.order_by('-created_date')

class FacultyUpdateView(UpdateView):
    model = Faculty

    def get_queryset(self):
        return Faculty.objects.order_by('-name')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(CreateView):
    login_url = '/login/'

    redirect_field_name = 'schoolapp/post_list.html'

    form_class = PostForm

    model = Post

class CreateUpdatesView(CreateView):
    login_url = '/login/'

    redirect_field_name = 'schoolapp/updates_list.html'

    form_class = UpdatesForm

    model = Updates


class CreateFacultyView(CreateView):
    login_url = '/login/'

    redirect_field_name = 'schoolapp/faculty_list.html'

    form_class = FacultyForm

    model = Faculty

class PostUpdateView(UpdateView):
    login_url = '/login/'

    redirect_field_name = 'schoolapp/post_detail.html'

    form_class = PostForm

    model = Post

class DraftListView(ListView):
    login_url = '/login/'
    model = Post

    def get_queryset(self):

        return Post.objects.filter(published_date__isnull = True).order_by('created_date')


class PostDeleteView(DeleteView):

    model = Post

    success_url = reverse_lazy('post_list')

class FacultyDeleteView(DeleteView):
    model = Faculty

    success_url = reverse_lazy('faculty_list')

class UpdatesDeleteView(DeleteView):
    model = Updates

    success_url = reverse_lazy('update_list')

class CreateGallaryView(CreateView):
    login_url = '/login/'

    model = Gallary

    redirect_field_name = 'schoolapp/gallary_list'

    form_class = GallaryForm


class GallaryDeleteView(DeleteView):
    login_url = '/login/'

    model = Gallary

    success_url = reverse_lazy('gallary_list')


class CreateFaqView(CreateView):
    login_url = '/login/'

    model = Faq

    redirect_field_name = 'schoolapp/faq_list'

    form_class = FaqForm


class FaqDeleteView(DeleteView):
    login_url = '/login/'

    model = Faq

    success_url = reverse_lazy('faq_list')


class FaqUpdateView(UpdateView):
    login_url = '/login/'

    model = Faq

    redirect_field_name = 'schoolapp/faq_list'

    form_class = FaqForm

class FaqListView(ListView):
    login_url = '/login/'

    model = Faq

    def get_queryset(self):
        return Faq.objects.order_by('-published_date')

class GallaryListView(ListView):
    login_url = '/login/'
    model = Gallary

    def get_queryset(self):
        return Gallary.objects.order_by('-created_date')


class ExamListView(ListView):
    model = Exam

    template_name = 'acheivements.html'

    def get_queryset(self):
        return Exam.objects.order_by('-created_date')


class ExamDetailView(DetailView):
    model = Exam



class CreateExamView(LoginRequiredMixin,CreateView):
    login_url = '/login/'

    model = Exam

    redirect_field_name = 'schoolapp/exam_list'

    form_class = ExamForm



class ExamDeleteView(DeleteView):
    model = Exam

    success_url = reverse_lazy('exam_list')


class SectionDeleteView(DeleteView):
    model  = Section

    success_url = reverse_lazy('section_list')


class CreateSectionView(LoginRequiredMixin,CreateView):
    login_url = '/login/'

    model = Section

    redirect_field_name = 'schoolapp/section_list'

    form_class = SectionForm


class SectionDetailView(DetailView):
    model = Section


class SectionListView(ListView):
    model = Exam

    def get_queryset(self):
        return Exam.objects.order_by('-created_date')


##########################################################################################################
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def add_achiever_to_exam(request,pk):
    exam = get_object_or_404(Exam,pk=pk)
    if request.method == "POST":
        form = AcheiverForm(request.POST)
        if form.is_valid():
            acheiver = form.save(commit=False)
            acheiver.exam = exam
            acheiver.save()
            return redirect('exam_detail',pk=pk)
    else:
        form = AcheiverForm()
    return render(request,'schoolapp/acheiver_form.html',{'form':form})

@login_required
def acheiver_delete(request,pk):
    acheiver = get_object_or_404(Acheiver,pk=pk)
    acheiver_pk = acheiver.exam.pk
    acheiver.delete()
    return redirect('exam_detail',pk=acheiver_pk)

@login_required
def add_student_to_section(request,pk):
    section = get_object_or_404(Section,pk=pk)
    if request.method == "POST":
        form = SectionForm(request.POST)
        if form.is_valid():
            students = form.save(commit = False)
            students.section = section
            students.save()
            return redirect('section_detail',pk=pk)
    else:
        form = SectionForm()
    return render(request,'schoolapp/section_form.html',{'form':form})


@login_required
def student_delete(request,pk):
    students = get_object_or_404(Section,pk=pk)
    students_pk = students.section.pk
    students.delete()
    return redirect('section_detail',pk=students_pk)



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm( data = request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('post_list')
        else:
            return redirect('post_list')
    else:
        form = PasswordChangeForm(user = request.user)

        args = {'form':form}

        return render(request,'schoolapp/change_password.html',args)


def sendingrequest(request):
    if request.method == 'POST':
        request_form = SendRequestForm(request.POST)
        if request_form.is_valid():
            test = request_form.save()
            studentname = request_form.cleaned_data['studentname']
            email = request_form.cleaned_data['email']

            test.save()

            value = True

            if value is None:
                messages.error(request, 'enter valid email')

            else:
                emails = EmailMessage('regarding the application submissioin',
                                     email+"\n\n"+studentname,to=[
                                     'anjansrivathsav1997',
                                     '201551048@iiitvadodara.ac.in'
                                     ])
                emails.send()

                emails = EmailMessage('regarding the application submission',
                                     'hey'+ studentname+",/n/n"+ "your application is successfully submitted",
                                     to=[email])

                emails.send()

                return HttpResponseRedirect(reverse('schoolapp/post_list'))
        else:
            return redirect('schoolapp/post_list.html')

    else:
        request_form = SendRequestForm()

    return render(request,'sendrequest.html',{'request_form':request_form})


class AlumniListView(ListView):
    model = Alumni

    def get_queryset(self):
        return Alumni.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class AlumniDetailView(DetailView):
    model = Alumni


class CreateAlumniView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'schoolapp/alumni_detail.html'

    form_class = AlumniForm

    model = Alumni


class AlumniUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/alumni_detail.html'

    form_class = AlumniForm

    model = Alumni



class AlumniDeleteView(LoginRequiredMixin,DeleteView):
    model = Alumni
    success_url = reverse_lazy('alumni_list')

########################################################


@login_required
def alumni_publish(request, pk):
    alumni = get_object_or_404(Alumni, pk=pk)
    alumni.publish()
    return redirect('alumni_detail', pk=pk)

@login_required
def add_alumnistudent_to_alumni(request, pk):
    alumni = get_object_or_404(Alumni, pk=pk)
    if request.method == "POST":
        form = AlumniStudentForm(request.POST)
        if form.is_valid():
            alumnistudent = form.save(commit=False)
            alumnistudent.alumni = alumni
            alumnistudent.save()
            return redirect('alumni_detail', pk=alumni.pk)
    else:
        form = AlumniStudentForm()
    return render(request, 'schoolapp/alumnistudent_form.html', {'form': form})


@login_required
def alumnistudent_approve(request, pk):
    alumnistudent = get_object_or_404(AlumniStudent, pk=pk)
    alumnistudent.approve()
    return redirect('alumni_detail', pk=alumnistudent.alumni.pk)


@login_required
def alumnistudent_remove(request, pk):
    alumnistudent = get_object_or_404(AlumniStudent, pk=pk)
    alumni_pk = alumnistudent.alumni.pk
    alumnistudent.delete()
    return redirect('alumni_detail', pk=alumni_pk)
