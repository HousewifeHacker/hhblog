import os
import sys
import re
import transaction
from getpass import getpass

from hiero.formatters import get_formatter
from sqlalchemy import engine_from_config
from sqlalchemy import create_engine
from datetime import datetime

from pyramid.paster import get_appsettings
from pyramid.paster import setup_logging

from hhblog.models import (
    DBSession,
    Base,
    Entry,
    User,
    Group,
    Category,
  #  Tag
)

def main():
    if len(sys.argv) != 3:
        print('Not how you use this!')
        sys.exit(1)

    config_uri = sys.argv[1]

    path = os.path.abspath(sys.argv[2])

    setup_logging(config_uri)
    settings = get_appsettings(config_uri)

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    username = raw_input("What is your username?: ").decode('utf-8')
    email = raw_input("What is your email?: ").decode('utf-8')
    password = getpass("What is your password?: ").decode('utf-8')

    with transaction.manager:
        admin_group = Group(
            name = 'admin',
            description = 'admin group'
        )

        admin = User(
            username=username,
            email=email,
            password=password
        )

        DBSession.add(admin_group)

        admin.groups.append(admin_group)

        DBSession.add(admin)
        DBSession.flush()

        cat1 = Category(
            title='Python',
            slug='python'
        )

        cat2 = Category(
            title='Reading',
            slug='reading'
        )

        cat3 = Category(
            title='Startup',
            slug='startup'
        )

        DBSession.add_all([cat1, cat2, cat3])

        for fname in os.listdir(path):
            if not fname.endswith('.rst'):
                continue

            with open(os.path.join(path, fname)) as f:
                lines = f.readlines()

                title = lines[0].strip()
                category = None
                tags = None
                status = True
                regex = '^:(.+):(.+)$'
                index = 2
                added_tags = []

                while True:
                    line = lines[index]
                    if line.strip() != '':
                        match = re.match(regex, line)
                        if match:
                            name = match.group(1)
                            value = match.group(2).strip()

                            if name == 'category':
                                if value == 'Code':
                                    category = cat1
                                if value == 'Startup':
                                    category = cat3
                                if value == 'Reading List':
                                    category = cat2
                            elif name == 'date':
                                mydate = value
                                date = datetime.strptime(mydate, "%Y-%M-%d")
                          #  elif name == 'tags':
                          #      tags = value.split(', ')
                          #      for tag in tags:
                          #          if tag in added_tags:
                          #              tag = tag.replace(' ','_')
                          #              break
                          #          else:
                          #              new = Tag(title=tag.replace(' ', '_'))
                          #              DBSession.add(new)
                          #              DBSession.commit()
                          #              added_tags.append(tag)
                          #              break
                            elif name == 'status':
                                if value == 'draft':
                                    status = False
                        else:
                            # no more metadata with beginning colons
                            break

                    index += 1

                body = ''.join(lines[index:])
                print 'title %s' % title
                print 'category %s' % category
                print 'date %s' % date
                print 'status %s' % status
                print 'tags %r' % tags
        #        print 'body %s' % ''.join(body)
                print 'admin %r' % admin

                formatter = get_formatter('rst')
#
                entry = Entry(
                    title=title,
                    content=body,
                    html_content=formatter(body).get_html(),
                    category=category,
                    published_on=date,
                    is_published=status,
                    owner=admin
                )

                DBSession.add(entry)

if __name__ == "__main__":
    main()
