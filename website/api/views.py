from braces.views import CsrfExemptMixin
from constance import config
from django.views.generic import TemplateView


class MainPageView(CsrfExemptMixin, TemplateView):
    template_name = "main_page.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["GOOGLE_MAP_URL"] = config.GOOGLE_MAP_URL
        return context
