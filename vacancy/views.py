from django.shortcuts import render, redirect, get_object_or_404
from .forms import VacancyForm
from django.contrib.auth.decorators import login_required
from .models import Vacancy
# Create your views here.


@login_required
def create_vacancy(request):
    if not hasattr(request.user, 'companyprofile'):
        return render(request, 'error.html', {'massage': 'Faqat kompaniyalar vakansiya yarata oladi!'})

    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)


            vacancy.company = request.user.companyprofile

            vacancy.save()
            return redirect('dashboard')
    else:
        form = VacancyForm()
    return render(request, 'vacancies/vacancy_form.html', {'form': form})

def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'vacancies/vacancy_detail.html', {'vacancy': vacancy})


def vacancy_list(request):
    vacancies = Vacancy.objects.order_by('-id')
    return render(request, 'vacancies/vacancy_list.html', {'vacancies': vacancies})