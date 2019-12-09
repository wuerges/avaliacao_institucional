from itertools import chain
from django.contrib import admin
from django import forms
from django.contrib.auth.models import User

# Register your models here.
from .models import Answer, QuestionTemplate, Question, Professor, \
    Semester, Major, Offer, Course, Professor, FormTemplate, \
        FormApplication

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # form = CourseForm
    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(major__in=request.user.major.all())

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == 'major':
            # kwargs["queryset"] = Major.objects.filter(profile=request.user.profile)
            kwargs["queryset"] = request.user.major.all() #Major.objects.filter(profile=request.user.profile)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    # form = CourseForm
    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == 'user':
            kwargs["queryset"] = User.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(FormApplication)
class FormApplicationAdmin(admin.ModelAdmin):
    # form = CourseForm
    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(semester__major__in=request.user.profile.major.all())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == 'semester':
            kwargs["queryset"] = Semester.objects.filter(major__in=request.user.profile.major.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    # form = CourseForm
    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(major__in=request.user.profile.major.all())



@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    # form = CourseForm
    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(major__in=request.user.profile.major.all())

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == 'major':
            kwargs["queryset"] = Major.objects.filter(profile=request.user.profile)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    # form = CourseForm
    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(major__in=request.user.profile.major.all())

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        
        if not request.user.is_superuser and db_field.name == 'professors':
            majors = request.user.profile.major.all()
            kwargs["queryset"] = Professor.objects.filter(majors__in=majors)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Answer)
admin.site.register(QuestionTemplate)
admin.site.register(Question)
# admin.site.register(Semester)
# admin.site.register(Major)
# admin.site.register(Offer)
# admin.site.register(Course)
# admin.site.register(Professor)
admin.site.register(FormTemplate)
# admin.site.register(FormApplication)
