the intention of this application is to enable static app files (css, js, pics) in the app folder itself.

<application1>/media/js/script.js

<application2>/media/js/script.js
<application2>/media/js/script2.js

the application should provide a command extension for generating the media folder for deploying on the webserver.
warnings of dublicate files should be raised
 
 
This view assumes a django application stores its media in app/media (which is very common) and the file is referred 
to in the templates by the last part of a django app path. e.g. As in django.contrib.admin -> 'admin'.

First we check if the media is a request in an application directory; if so we attempt to serve it from there. 
Then we attempt to provide the document from the document_root parameter (if provided).

To use this view you should add something like the following to urls.py: 

if settings.DEBUG: urlpatterns += (r'^media/(?P<path>.*)$', 'site.media.serve_apps', {'document_root' : settings.MEDIA_ROOT}) 

You can then have the admin media files served by setting ADMIN_MEDIA_PREFIX = '/media/admin/' 