from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.admin.util import unquote

from erroneous.models import Error


class ErrorAdmin(admin.ModelAdmin):
    list_display = ('path', 'kind', 'info', 'when',)
    list_display_links = ('path',)
    ordering = ('-id',)
    search_fields = ('path', 'kind', 'info', 'data')
    readonly_fields = ('path', 'kind', 'info', 'data', 'when', 'html',)
    fieldsets = (
        (None, {
            'fields': ('kind', 'path', 'info', 'when')
        }),
    )
    change_form_template = 'erroneous/admin_change_form.html'

    def has_delete_permission(self, request, obj=None):
        """
        Disabling the delete permissions
        """
        return True

    def has_add_permission(self, request):
        """
        Disabling the create permissions
        """
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
        The detail view of the error record.
        """
        obj = self.get_object(request, unquote(object_id))
        extra_context = extra_context or {}
        extra_context.update({
            'instance': obj,
            'error_body': mark_safe(obj.html),
        })

        return super(ErrorAdmin, self).change_view(request, object_id, form_url, extra_context)

admin.site.register(Error, ErrorAdmin)