from django.conf import settings
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# we extend INSTALLED_APPS here.
# Any apps you want to install you can
# just add here (or use app.py)
settings.INSTALLED_APPS.extend([
    'rest_framework',    
    'api',
    'rest_framework_swagger',
])

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',        
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        #'tokenauth.authbackends.RESTTokenAuthBackend',        
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
}

SWAGGER_SETTINGS = {
    'is_authenticated': True,
    'permission_denied_handler': 'api.permissions.swagger_permission_denied_handler',
    'info': {
        'contact': 'youremail@tangentsolutions.co.za',
        'title': 'LeaveService API',
        'description': """
Welcome to the docs for the LeaveService

<h2>Authentication</h2>

<p>This API users TOKEN authentication. 
Get the token for an existing user, 
and make sure to add the AUTHORIZATION header to all rquests.
</p>
e.g.:<br/>
<pre><code>curl -X GET http://127.0.0.1:8000/users/ \\
  -H 'Authorization: Token 1234...'
</code></pre>

""",        
    },
}
 
 
STATIC_ROOT = '/code/static/'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--with-spec', 
             '--with-coverage', '--cover-html', '--cover-erase', '--with-xunit', 
             '--cover-xml', '--cover-xml-file=reports/coverage.xml',
             '--cover-package=.', '--cover-html-dir=reports/cover', '-s']

