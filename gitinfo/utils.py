from django.core.exceptions import ImproperlyConfigured
import datetime
import git
import json

formats = (
    ('hash', '%H'),
    ('subject', '%s'),
    ('sanitized_subject', '%f'),
    ('body', '%b'),
    ('commiter_name', '%cn'),
    ('commiter_date', '%cd'),
)


def format_formats(f):
    ff = ','.join(['"{0}":"{1}"'.format(x[0], x[1]) for x in formats])
    return '{' + ff + '}'


formatted_formats = format_formats(formats)


def parse_date(d):
    return datetime.datetime.strptime(d, "%Y-%m-%dT%H:%M:%S")


def get_git_info():
    try:
        r = git.Repo(search_parent_directories=True)
        git_resp = r.git.log(pretty=formatted_formats, n=1, date='format:%Y-%m-%dT%H:%M:%S')
        git_resp = git_resp.replace('\n', '\\n')
        json_resp = json.loads(git_resp)
        json_resp['body'] = json_resp['body'].replace('\\n', '\n')
        json_resp['commiter_date'] = parse_date(json_resp['commiter_date'])

        return json_resp
    except AttributeError:
        raise ImproperlyConfigured(
            "Same error with getting attr about git commit")
