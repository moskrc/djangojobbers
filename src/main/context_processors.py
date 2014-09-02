from django.contrib.sites.models import Site


def main_processor(request):
    return {'site':Site.objects.get_current()}