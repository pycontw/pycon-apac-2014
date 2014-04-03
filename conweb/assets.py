from django_assets import Bundle, register
pycontw_css = Bundle(
    'all.css',
    filters='cssmin',
    output='build/pycontw-%(version)s.css')
register('pycontw_css', pycontw_css)
