import sys
import re

# For @license tags only add them if the license is chosen. We don't want to
# need to duplicate the conditional logic everywhere, so
# cookiecutter.__license_tag contains the newline and then the full line of
# the tag (or an empty string if none was chosen) suitable for PHP and JS files
# This looks like python code, but its actually using
# https://jinja.palletsprojects.com/en/3.1.x/templates/#if-expression
{{
    cookiecutter.update({
        '__license_tag': '\n * @license ' + cookiecutter.license
                            if cookiecutter.license != 'none'
                            else ''
    })
}}

KEBAB_CASE_REGEX = r'^[a-z][-a-z]+?$'

# Validation of some inputs
def requireKebab(optionVal, optionName):
    # Only validate if provided, for user rights
    if optionVal == '':
        return

    if not re.match(KEBAB_CASE_REGEX, optionVal):
        print('ERROR: option `%s` must be formatted in kebab case' % optionName)
        sys.exit(1)

requireKebab('{{ cookiecutter.user_right }}', 'user_right')