from .models import AcademicYear, AcademicTerm


def site_defaults(request):
    current_year = AcademicYear.objects.get(current=True)
    current_term = AcademicTerm.objects.get(current=True)
    contexts = {
        "current_year": current_year.name,
        "current_term": current_term.name,
    }

    return contexts
