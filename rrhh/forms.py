from tabnanny import verbose
from tkinter.tix import Select
from django import forms
from django.forms import fields
from django.utils.translation import ugettext_lazy as _

from .models import JobDescription, Recruitment

class AddJobDescriptionForm(forms.ModelForm):

    class Meta:
        model = JobDescription
        fields = [
            _('createdBy'), 
            _('creationDate'), 
            _('code'),
            _('title'), 
            _('departament'), 
            _('reportTo'),
            _('jobDescription'), 
            _('responsabilities'), 
            _('skills'),
            _('abilities'),
            _('experience'),
            _('educationRequirements'),
            _('knowledge'),
            _('annualSalary')]
        help_texts = {'': None,}
        verbose_name = [
            _('Created by'), 
            _('Creation date'), 
            _('Code'), 
            _('Title'), 
            _('Departament'),
            _('Report to'),
            _('Job description'),
            _('Responsabilities'),
            _('Skills'),
            _('Abilities'),
            _('Experience'),
            _('Education requirements'),
            _('Knowledge'),
            _('Annual salary')]

class AddRecruitmentForm(forms.ModelForm):

    class Meta:
        model = Recruitment
        fields = [
            _('requester'), 
            _('dateOfRequest'), 
            _('departament'), 
            _('jobDescription'),
            _('startingDate'),
            _('numberOfVacancies'),
            _('title'),
            _('responsabilities'),
            _('location'),
            _('comments')]
        help_texts = {'requester': None,}
        verbose_name = [
            _('Requester'),
            _('Date of request'),
            _('Departament'),
            _('Job description'),
            _('Starting date'),
            _('Number of vacancies'),
            _('Title'),
            _('Responsabilities'),
            _('Location'),
            _('Comments')]