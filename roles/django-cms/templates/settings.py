# This file is generated by django-cms ansible installer ({{ template_run_date }})
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.{{ database }}{% if db == "sqlite" %}3{% endif %}',
		'NAME': '{{ db_name }}',
		'USER': '{% if db != "sqlite" %}{{ db_name }}{% endif %}',
		'PASSWORD': '{% if db != "sqlite" %}{{ db_password }}{% endif %}',
	}
}