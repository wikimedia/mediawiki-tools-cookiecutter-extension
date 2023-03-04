# cookiecutter-mediawiki-extension

This provides a template to create new MediaWiki extension using the
[cookiecutter project](https://github.com/cookiecutter/cookiecutter).

After installing cookiecutter, run:
```
cookiecutter gh:WikiTeq/cookiecutter-mediawiki-extension
```

For example, the following would create the folder
`mediawiki-extensions-UserWatch`, for an extension named `UserWatch` that
- requires MediaWiki 1.39 or later to run
- adds a new user right, `watch-users` (granted to administrators by default)
- creates a special page, `Special:WatchUser`
- has a database schema that should be applied (the actual schema would still
need to be created)
- is licensed under GPL-2.0-or-later

```
repo_name [mediawiki-extensions-example]: mediawiki-extensions-UserWatch
extension_name [ExampleExtension]: UserWatch
description [A short description of the extension.]: Allow watching changes by users
author_name [Your Name]: Daniel Scherzer
Select license:     
1 - GPL-2.0-or-later
2 - GLP-2.0-only    
3 - WTFPL
4 - none
Choose from 1, 2, 3, 4 [1]: 1
minimum_mw [1.35.0]: 1.39
has_database_schemas [False]: yes
special_page [Name of special page (leave blank to omit)]: WatchUser
user_right [Name of user right to create (leave blank to omit)]: watch-users
Select add_right_to_group:
1 - none
2 - *
3 - user
4 - sysop
Choose from 1, 2, 3, 4 [1]: 4
```