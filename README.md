# django-cms via Ansible
Deploy virtualenv + django-cms + nginx + DB (sqlite3|MySQL) + uwsgi via ansible.

(tested only on Ubuntu 14.04, django-cms stable (3.1.2))

1) Djando-cms installs via recommended "djangocms -p . my_site"
2) Standart nginx.
3) MySQL or sqlite3 database.
4) Standart uwsgi.

All components uses recommended paths:
* `/etc/nginx/sites-available` and `/etc/nginx/sites-enabled`
* `/etc/uwsgi/apps-available` and `/etc/uwsgi/apps-enabled`

# HOW TO

You mast have ansible installed (`apt-get install ansible`).
Use preinstalled scripts. Scripts with '.local' must be used if you work on localhost.

## 1. Edit site config and `hosts`
* Edit `sites/default.yml` config or create your own. `sites/my_site.yml` for example.
* If you use ansible remotely, edit `hosts` file.

## 2. Prepare server
Run once prepare ansible role `bin/prepare` or `bin/prepare.local`

## 3. Prepare Database
### Sqlite3
* Very carefull do nothing.
### Mysql
* If you have production MySQL with `/root/.my.cnf`, do nothing and skip mysql section.
* For clean servers run `bin/mysql` or `bin/mysql.local`
* If you do not remember MySQL root password or you want to reset it, run `bin/mysql reset` or `bin/mysql.local reset`

## 4. Install django-cms
* If you want to use `sites/default.yml`, run `bin/django-cms` or `bin/django-cms.local`.
* If you want to use `sites/my_site_.yml`, run `bin/django-cms my_site` or `bin/django-cms.local my_site`.

After it you will get fully configured and launched site. Profit.

#Notes
* Uwsgi runs under nginx user and group. See `/etc/nginx/nginx.conf`
* No additional scripts to run after reboot needed.
* All logs (nginx,uwsgi) wiil rotate automatically if logrotate installed.
* Local settings.py with database config will be created and included to main settings.py.
* Bonus: mysql and files backup script included.
* You can use `bin/play` script to run ansible (Usage: `./play (host) (site) (role1) [role2] ... [role6]`).

#Site config Example
```
---
# default.yml — default site config. Edit freely.
##################
# Mandatory params

# base dir with sites and common virtualenv
project: "projects"

# unix user with sites
user_uid: "www"

# base site url
url: "foofoofoo.me"

# Database engine
# (mysql|sqlite) default:sqlite
db: "mysql"

# virtualenv/bin/djangocms params
# deafult: "Europe/Moscow"
timezone: "Europe/Moscow"

# CMS languages
languages: "en,ru"

# 1.4,1.5,1.6,1.7,1.8,stable
django_version: "stable"

# 2.4,3.0,3.1,stable,develop
cms_version: "stable"

# install bootstrap
bootstrap: "no"

# Superuser login
admin_username: "foo"
# Superuser email
admin_email: "foo@foofoofoo.me"
# Superuser passowrd
admin_pass: "foofoofoo"

# Virtualenv dir
virtualenv_dir: ".env"

#################
# Optional params

# Site aliases space separated
url_aliases: "foofoofoo.net foofoofoo.org"

# Sertificates country
# RU,US etc default: RU
sert_country: "US"

# Sertificates company
# default: site url
sert_company: "Foo monsters"
```
