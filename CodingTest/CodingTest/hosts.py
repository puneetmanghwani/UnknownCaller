from django.conf import settings
from django_hosts import patterns, host



host_patterns = patterns(
    '',
    # Admin Urls
    host('admin', 'CodingTest.admin_urls', name='admin'),
    # Api Urls
    host('api', 'CodingTest.api_urls', name='api'),
)
