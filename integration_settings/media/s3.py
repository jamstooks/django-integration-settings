"""
    AASHE's shared media config
"""
import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", None)

AWS_QUERYSTRING_AUTH = False  # Prefer unsigned S3 URLs.

# User uploaded media
DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = os.environ.get("DEFAULT_S3_PATH", 'uploads')
MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/%s/' % (
    AWS_STORAGE_BUCKET_NAME, DEFAULT_S3_PATH)

# Static files, served with whitenoise
STATIC_ROOT = 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_URL = '/static/'

# CDN Settings
CDN_STATIC_HOST = os.environ.get('CDN_STATIC_HOST', None)
if CDN_STATIC_HOST:
    STATIC_URL = "//%s%s" % (CDN_STATIC_HOST, STATIC_URL)

CDN_MEDIA_HOST = os.environ.get('CDN_MEDIA_HOST', None)
if CDN_MEDIA_HOST:
    MEDIA_URL = '//%s/%s/' % (
        CDN_MEDIA_HOST, DEFAULT_S3_PATH)
    AWS_S3_CUSTOM_DOMAIN = CDN_MEDIA_HOST

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
