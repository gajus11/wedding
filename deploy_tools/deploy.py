import os
import random
import subprocess
from optparse import OptionParser

REPO_URL = 'https://lgajownik@bitbucket.org/lgajownik/wedding.git'
USER_NAME = 'lukasz-gajownik'
DOMAIN_NAME = 'gajownik.com'
PROJECT_NAME = 'wedding'
SITE_NAME = 'slub'
PYTHON_VERSION='3.5'

def deploy(user=USER_NAME,repo=REPO_URL, project=PROJECT_NAME, domain_name=DOMAIN_NAME, site_name=SITE_NAME, db_password='', python_version=PYTHON_VERSION):
    domain_folder = '/usr/home/%s/domains' % (user)
    subdomain_name = '%s.%s' % (site_name, domain_name)
    site_folder = '%s/%s/public_python' % (domain_folder, subdomain_name)
    virtualenv_folder = '/usr/home/%s/.virtualenvs/%s' % (user, subdomain_name)

    print('domain_folder: ' + domain_folder)
    print('site_folder: ' + site_folder)
    print('subdomain_name: ' + subdomain_name)
    print('virtualenv_folder: ' + virtualenv_folder)
    print('repo: ' + repo)
    print('user: ' + user)

    _create_mydevil_dns(domain_name, subdomain_name)
    _create_site_folder_if_neccessary(site_folder)
    _create_virtualenv_if_neccessary(virtualenv_folder, user, subdomain_name, python_version)
    _create_mydevil_site(subdomain_name, virtualenv_folder, python_version)
    _create_postgresql_db_if_neccessary(site_name)
    _get_latest_source(site_folder, repo)
    _create_directory_structure_if_necessary(site_folder)
    _update_virtualenv(site_folder, virtualenv_folder, domain_name, user, python_version)
    _update_settings(site_folder, project, subdomain_name, site_name, db_password)
    _update_static_files(site_folder, virtualenv_folder, python_version)
    _update_database(site_folder, virtualenv_folder, python_version)
    _create_passenger_wsgi_if_neccessary(site_folder, project)

def _create_mydevil_dns(domain_name, subdomain_name):
    print('_create_mydevil_dns')
    deafult_ovh_address = '85.194.241.231'
    _execude_command('devil dns add %s %s A %s' % (
        domain_name, subdomain_name, deafult_ovh_address
    ))

def _create_site_folder_if_neccessary(site_folder):
    print('_create_site_folder_if_neccessary')
    if not os.path.exists(site_folder):
        _execude_command('mkdir -p %s' % (site_folder))

def _create_virtualenv_if_neccessary(virtualenv_folder, user, subdomain_name, python_version):
    print('_create_virtualenv_if_neccessary')
    if not os.path.exists(virtualenv_folder):
        _execude_command('cd /home/%s/.virtualenvs && virtualenv %s -p /usr/local/bin/python%s' % (
            user, subdomain_name,python_version
        ))

def _create_mydevil_site(subdomain_name, virtualenv_folder, python_version):
    print('_create_mydevil_site')
    _execude_command('devil www add %s python %s/bin/python%s' % (
        subdomain_name, virtualenv_folder, python_version
    ))

def _create_postgresql_db_if_neccessary(site_name):
    print('_create_postgresql_db_if_neccessary')
    command = 'devil pgsql list'
    result = subprocess.check_output(command, shell=True)
    if not site_name in result:
        _execude_command('devil pgsql db add %s' % (site_name))

def _get_latest_source(site_folder, repo):
    print('_get_latest_source')
    if not os.path.exists(site_folder + '/.git'):
        _execude_command('rm -rf %s' % (site_folder))
        _execude_command('git clone %s %s' % (repo, site_folder))
    else:
        _execude_command('cd %s && git fetch' % (site_folder))
    _execude_command('cd %s' % (site_folder))
    current_commit = os.popen('git log -n 1 --format=%H').read()
    _execude_command('cd %s && git reset --hard %s' % (site_folder, current_commit))

def _create_directory_structure_if_necessary(site_folder):
    print('_create_directory_structure_if_necessary')
    for subfolder in ('public', '../database', 'public/static', 'public/media'):
        if not os.path.exists('%s/%s' % (site_folder, subfolder)):
            _execude_command('mkdir -p %s/%s' % (site_folder, subfolder))

def _update_virtualenv(site_folder, virtualenv_folder, domain_name, user, python_version):
    print('_update_virtualenv')
    _execude_command('source %s/bin/activate' % (virtualenv_folder))
    _execude_command('%s/bin/pip%s install -r %s/requirements.txt' % (
        virtualenv_folder, python_version, site_folder
    ))

def _update_settings(site_folder, project, subdomain_name, site_name, db_password):
    print('_update_settings')
    settings_path = site_folder + '/%s/settings.py' % (project)
    _inplace_change(settings_path, "DEBUG = True", "DEBUG = False")
    # working with SECRET_KEY from dedicated file
    _inplace_change(settings_path, "#SECRET_KEY = ", "SECRET_KEY = ")   # For not creating something like ########SECRET_KEY
    _inplace_change(settings_path, "SECRET_KEY = ", "#SECRET_KEY = ")
    # add secret key file
    secret_key_file = site_folder + '/%s/secret_key.py' % (project)
    if not os.path.exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = "".join(random.SystemRandom().choice(chars) for _ in range(50))
        _append_to_file(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    _append_to_file(settings_path, '\nfrom .secret_key import SECRET_KEY')

    _inplace_change(settings_path,
        'ALLOWED_HOSTS = .+$',
        'ALLOWED_HOSTS = ["%s"]' % (subdomain_name,)
    )

    # change database engine
    database_setting_file = site_folder + '/%s/database_setting.py' % (project)
    if not os.path.exists(database_setting_file):
        new_database_setting = "" \
            "DATABASES = { \n" \
                "\t'default': { \n" \
                    "\t\t'ENGINE': 'django.db.backends.postgresql',\n" \
                    "\t\t'NAME': 'p1350_%s',\n" \
                    "\t\t'USER': 'p1350_%s', \n" \
                    "\t\t'PASSWORD': '%s', \n" \
                    "\t\t'HOST': 'pgsql8.mydevil.net', \n"\
                    "\t\t'PORT': '5432',\n" \
                "\t}\n" \
            "\n}" % (site_name, site_name, db_password)
        _append_to_file(database_setting_file, new_database_setting)
    _append_to_file(settings_path, '\nfrom .database_setting import DATABASES')

    _inplace_change(settings_path, 'DATABASES = {', 'DEPRECATED_SETTINGS = {')

def _update_static_files(site_folder, virtualenv_folder, python_version):
    print('_update_static_files')
    _execude_command('cd %s && %s/bin/python%s manage.py collectstatic --noinput' % (
        site_folder, virtualenv_folder, python_version
    ))

def _update_database(site_folder, virtualenv_folder, python_version):
    print('_update_database')
    _execude_command('cd %s && %s/bin/python%s manage.py makemigrations' % (
        site_folder, virtualenv_folder, python_version
    ))
    _execude_command('cd %s && %s/bin/python%s manage.py migrate --noinput' % (
        site_folder, virtualenv_folder, python_version
    ))

def _create_passenger_wsgi_if_neccessary(site_folder, project):
    passanger_wsgi_file = '%s/passenger_wsgi.py' % (site_folder)
    if not os.path.exists(passanger_wsgi_file):
        passanger_wsgi_py = "" \
            "import sys, os \n" \
            "\n" \
            "sys.path.append(os.getcwd()) \n" \
            "os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings'\n" \
            "from django.core.wsgi import get_wsgi_application\n" \
            "application = get_wsgi_application()" % (project)
        _append_to_file(passanger_wsgi_file, passanger_wsgi_py)

def _execude_command(command):
    print('Execute: %s' % (command))
    os.system(command)

def _inplace_change(filename, old_string, new_string):
    s = open(filename).read()
    if old_string in s:
        s = s.replace(old_string, new_string)
        f = open(filename, 'w')
        f.write(s)
        f.flush()
        f.close()

def _append_to_file(filename, text):
    with open(filename, "a") as myfile:
        myfile.write(text)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--user",
                  action="store", dest="user", type='string', default=USER_NAME,
                  help="Username on server (default: lukasz-gajownik")
    parser.add_option("--repo",
                  action="store", dest="repo", type='string', default=REPO_URL,
                  help="Repository url (default: https://lgajownik@bitbucket.org/lgajownik/wedding.git")
    parser.add_option("--project",
                  action="store", dest="project", type='string', default=PROJECT_NAME,
                  help="Django project name (default: wedding")
    parser.add_option("--domain-name",
                  action="store", dest="domain_name", type='string', default=DOMAIN_NAME,
                  help="Domain name (default: gajownik.com")
    parser.add_option("--site-name",
                      action="store", dest="site_name", type='string', default=SITE_NAME,
                      help="Site name in domain (default: slub")
    parser.add_option("--python_version",
                      action="store", dest="python_version", type='string', default='3.5',
                      help="Python version (default 3.5)")
    parser.add_option("--db_password",
                      action="store", dest="db_password", type='string', default='',
                      help="Password for PostgreSQL")

    options, args = parser.parse_args()

    deploy(user=options.user,
           repo=options.repo,
           project=options.project,
           domain_name=options.domain_name,
           site_name=options.site_name,
           db_password=options.db_password,
           python_version=options.python_version)