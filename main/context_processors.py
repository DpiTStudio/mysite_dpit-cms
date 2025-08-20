from .models import SiteMetadata


def site_metadata(request):
    try:
        metadata = SiteMetadata.objects.filter(is_active=True).first()
        return {"site_metadata": metadata}
    except:
        return {"site_metadata": None}
