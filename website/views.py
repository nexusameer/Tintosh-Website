from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.views.generic import View
from .models import *
from .forms import *
from django.http import JsonResponse

# Create your views here.

class IndexPage(TemplateView):
    template_name = 'index-2.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        context['company'] = Company.load()
        context['testimonals'] = Testimonals.objects.all()
        context['teams'] = TeamMember.objects.all()
        context['clients'] = FeaturedClient.objects.all()
        context['skills'] = Skill.objects.all()
        context['categories'] = Portfolio.objects.values_list('project_category', flat=True).distinct()
        
        category = self.request.GET.get('category')
        if category:
            context['portfolio']=Portfolio.objects.filter(project_category=category)
        else:
            context['portfolio'] = Portfolio.objects.all()

        
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\nMessage: {message}",
                email,
                ['ameerh10fw@gmail.com'],
                fail_silently=False,
            )
            return redirect('index2')
        else:
            return render(request, 'index2.html', {'form': form, 'company': Company.load(), 'testimonals': Testimonals.objects.all(), 'teams': TeamMember.objects.all()})


class PortfolioView(TemplateView):
    template_name='portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonals'] = Testimonals.objects.all()

        category = self.request.GET.get('category')
        if category:
            context['portfolio']=Portfolio.objects.filter(project_category=category)
        else:
            context['portfolio'] = Portfolio.objects.all()

        context['categories'] = Portfolio.objects.values_list('project_category', flat=True).distinct()
        return context


class FilterPortfolioView(View):
    def get(self, request, *args, **kwargs):
        category = request.GET.get('category')
        if category:
            portfolio_items = Portfolio.objects.filter(project_category=category)
        else:
            portfolio_items = Portfolio.objects.all()

        portfolio_list = [{
            'name': item.name,
            'image_url': item.image.url,
            'url': item.url,
        } for item in portfolio_items]

        return JsonResponse({'portfolio': portfolio_list})
        

class TeamView(TemplateView):
    template_name = 'team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = TeamMember.objects.all()
        return context

class ContactFormView(TemplateView):

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        company = Company.load()
        return render(request, 'contact.html', {'form': form, 'company':company})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\nMessage: {message}",
                email,
                ['ameerh10fw@gmail.com'],
                fail_silently=False,
            )
            return redirect('contact')
        else:
            return HttpResponse('Form is not valid', status=400)

class AboutView(TemplateView):
    template_name='about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = TeamMember.objects.all()
        context['company'] = Company.load()
        context['clients'] = FeaturedClient.objects.all()
        return context

class Service(TemplateView):
    template_name = 'service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = TeamMember.objects.all()
        context['skills'] = Skill.objects.all()
        context['company'] = Company.load()
        context['testimonals'] = Testimonals.objects.all()
        context['clients'] = FeaturedClient.objects.all()

        return context

