def site(request):
    # Site info preprocessor 
    context = {}
    context['SITE_TITLE'] = 'Dev2tech'
    context['SITE_URL'] = ''
    return context

def menu(request):
    # Menu preprocessor 
    context = {}
    return context


def sessions(request):
    # Cookies prepeocessor
    context = {}
    return context