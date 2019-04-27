from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.db.models.query_utils import Q

from featured.models import Featured, Category


class FeaturedAdminForm(forms.ModelForm):
    class Meta:
        model = Featured
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FeaturedAdminForm, self).__init__(*args, **kwargs)
        q = Q()
        for app, model in settings.FEATURABLE_MODELS:
            q.add(Q(model=model, app_label=app), Q.OR)
        self.fields['content_type'].queryset = self.fields['content_type'].queryset.filter(q)


class FeaturedAdmin(admin.ModelAdmin):
    form = FeaturedAdminForm
    list_display = ['content_object', 'content_type', 'object_id', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'active']


admin.site.register(Featured, FeaturedAdmin)
admin.site.register(Category, CategoryAdmin)
