the intention of this application is to enable static app files (css, js, pics) in the app folder itself.

<application1>/media/<application1>/js/script.js
<application2>/media/<application2>/js/script.js

<project>/media/logo.jpg

To use this view in development you should add something like the following to urls.py: 
if settings.DEBUG: urlpatterns += (r'^media/(?P<path>.*)$', 'site.media.serve_apps', {'document_root' : settings.MEDIA_ROOT}) 

For deployment there is a managament command called `symlinkmedia` that will create symlinks to each applications media directory in `MEDIA_ROOT`.

Now all apps in INSTALLED_APPS that have a "media" directory in them will be reachable as '/media/<application_name>/'.

You can then have the admin media files served by setting ADMIN_MEDIA_PREFIX = '/media/admin/' 