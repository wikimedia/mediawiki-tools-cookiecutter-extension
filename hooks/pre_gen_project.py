import sys
import re

# For @license tags only add them if the license is chosen. We don't want to
# need to duplicate the conditional logic everywhere, so
# cookiecutter.__license_tag contains the newline and then the full line of
# the tag (or an empty string if none was chosen) suitable for PHP and JS files
# Same with the options that we want the default to really be a prompt
# For some reason could not get boolean has_database_schemas to work with
# Jinja conditionals, manually convert to 'YES' or empty string
# This looks like python code, but its actually using
# https://jinja.palletsprojects.com/en/3.1.x/templates/#if-expression
{{
    cookiecutter.update({
        '__license_tag': '\n * @license ' + cookiecutter.license
                            if cookiecutter.license != 'none'
                            else '',
        '__special_page_name': cookiecutter.special_page
                                if cookiecutter.special_page !=
                                    'Name of special page (leave blank to omit)'
                                else '',
        '__sp_i18n_prefix': cookiecutter.__special_page_name.lower(),
        '__user_right_name': cookiecutter.user_right
                                if cookiecutter.user_right !=
                                    'Name of user right to create (leave blank to omit)'
                                else '',
        '__has_database_schemas': 'YES'
                                if cookiecutter.has_database_schemas.lower() in
                                    ['1', 'true', 't', 'yes', 'y', 'on']
                                else ''
    })
}}

KEBAB_CASE_REGEX = r'^[a-z][-a-z]+?$'
MW_MAJOR_REGEX = r'^1\.\d\d$'
MW_MINOR_REGEX = r'^1\.\d\d\.\d\d?$'

# Validation of some inputs
def requireKebab(optionVal, optionName):
    # Only validate if provided, for user rights
    if optionVal == '':
        return

    if not re.match(KEBAB_CASE_REGEX, optionVal):
        print('ERROR: option `%s` must be formatted in kebab case' % optionName)
        sys.exit(1)

def requireValidMWVersion(optionVal, optionName):
    # Must be provided, empty strings are still invalid
    if re.match(MW_MAJOR_REGEX, optionVal):
        return
    if re.match(MW_MINOR_REGEX, optionVal):
        return
    
    GOOD_FORMAT = '`1.xx`, `1.xx.x`, or `1.xx.xx`'
    print('ERROR: option `%s` must be formatted %s' % (optionName, GOOD_FORMAT))
    sys.exit(1)

def doValidation():
    requireKebab('{{ cookiecutter.__user_right_name }}', 'user_right')
    requireValidMWVersion('{{ cookiecutter.minimum_mw }}', 'minimum_mw' )

doValidation()