from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CandidateRegisterForm, CompanyRegisterForm
from .models import CompanyProfile, CandidateProfile
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from .models import Resume



def register_candidate(request):
    if request.method == 'POST':
        form = CandidateRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            CandidateProfile.objects.create(user=user)
            login(request, user)
            return redirect('dashboard')
    else:
        form = CandidateRegisterForm()
    return render(request, 'account/register_candidate.html', {'form': form})



def register_company(request):
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            CompanyProfile.objects.create(
                user=user,
                company_name=form.cleaned_data.get('company_name'),
            )
            login(request, user)
            return redirect('dashboard')
    else:
        form = CompanyRegisterForm()
    return render(request, 'account/register_company.html', {'form': form})



@login_required
def dashboard(request):
    user = request.user

    if hasattr(user, 'candidateprofile'):
        context = {
            'role': 'Candidate',
            'profile': user.candidateprofile,
            'resumes': user.candidateprofile.resume_set.all()
        }

    elif hasattr(user, 'companyprofile'):
        context = {
            'role': 'Company',
            'profile': user.companyprofile,
            'vacancies': user.companyprofile.vacancy_set.all()
        }

    else:
        context = {
            'role': 'Admin',
        }
    return render(request, 'account/dashboard.html', context)



@login_required
def create_resume(request):
    if not hasattr(request.user, 'candidateprofile'):
        return render(request, 'error.html', {'massage': 'Faqat nomzodlar rezyume yarata oladi!'})

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.profile = request.user.candidateprofile
            resume.save()
            return redirect('dashboard')
    else:
        form = ResumeForm()
    return render(request, 'resumes/resume_form.html', {'form': form})