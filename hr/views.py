from re import A
from django.db.models.query import InstanceCheckMeta
from django.http import request, JsonResponse, response, Http404
from django.shortcuts import get_object_or_404, reverse, redirect, render
from django.views import generic
from django.conf import settings 

from hr.forms import AddJobDescriptionForm, AddRecruitmentForm, ApproveRequestForm
from hr.models import JobDescription, Recruitment

class RecruitmentView(generic.FormView):
    form_class = AddRecruitmentForm
    template_name = "recruitmentRequest.html"

    def get_success_url(self):
        return reverse('hr:recruitment')

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
        return reverse('hr:jobDescription')

    def form_valid(self, form):
        job = form.save(commit=True)
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(JobDescriptionView, self).form_valid(form)

class ApproveRequestView(generic.FormView):
    form_class = ApproveRequestForm
    template_name = "approveRequest.html"

    def get_success_url(self):
        return reverse('hr:approveRequest')

    def get_object(self):
        return get_object_or_404(Recruitment, id=kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ApproveRequestView, self).get_context_data(**kwargs)
        #context['approveR'] = self.get_object()
        return context

    def form_valid(self, form):
        print("entro fv")
        def get(self, request, *args, **kwargs):
            print("----------------entro get-----------------")
            print(request)
            recruitment = get_object_or_404(Recruitment, id=kwargs['pk'])
            recruitment.requisitionApproved = True
            recruitment.approvalsComments = "no"
            recruitment.save()

        return super(JobDescriptionView, self).form_valid(form)