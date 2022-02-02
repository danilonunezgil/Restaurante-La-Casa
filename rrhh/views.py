from re import A
from django.db.models.query import InstanceCheckMeta
from django.http import request, JsonResponse, response, Http404
from django.shortcuts import reverse, redirect, render
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib import messages 

from rrhh.forms import AddJobDescriptionForm, AddRecruitmentForm
from rrhh.models import JobDescription, Recruitment

class RecruitmentView(generic.FormView):
    form_class = AddRecruitmentForm
    template_name = "recruitmentRequest.html"

    def get_success_url(self):
        return reverse('rrhh:recruitment')

    def form_valid(self, form):
        recruitment = form.save(commit=True)
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(RecruitmentView, self).form_valid(form)

class JobDescriptionView(generic.FormView):
    form_class = AddJobDescriptionForm
    template_name = "jobDescription.html"

    def get_success_url(self):
        return reverse('rrhh:jobDescription')

    def form_valid(self, form):
        job = form.save(commit=True)
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(JobDescriptionView, self).form_valid(form)