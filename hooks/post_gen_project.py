import sys
import os

# When no license is chosen no COPYING is created
NO_LICENSE_CHOICE = 'none'


# For some options (like special page) we want to allow either setting the
# option (special page name) or not using it at all.
# We cannot change the values in the cookiecutter options as part of this
# hook (unless we want the changes to be unconditional, i.e. not part of the
# python logic, using cookiecutter.update) so we have notes before them,
# and delete the files if they are unneeded afterwards
def conditionalFile(optionVal, fileName):
    # option is either a bool or a string
    optType = type(optionVal)
    if optType == bool and optionVal == True:
        return
    if optType == str and optionVal == '':
        return

    # Just in case something went wrong with the value, don't always delete
    if optType != bool and optType != str:
        print('ERROR: unknown option type %s!' % optType)
        sys.exit(1)

    if not os.path.exists(fileName):
        print('ERROR: cannot remove missing file %s!' % fileName)
        sys.exit(1)

    # Also used for directories
    if os.path.isdir(fileName):
        os.rmdir(fileName)
    else:
        os.unlink(fileName)

# In some files, we have conditional lines that result in some blank lines
# in the result, remove those
def removeBlankLines(fileName):
    if not os.path.exists(fileName):
        print('ERROR: cannot remove blank lines, missing file %s!' % fileName)
        sys.exit(1)

    with open(fileName, 'r') as f:
        text = f.read()
    
    keepLines = [line for line in text.split('\n') if not line.isspace()]
    newText = '\n'.join(keepLines)

    with open(fileName, 'w') as f:
        f.write(newText)

# Handle whichever license was chosen, and delete the others
def processLicense(licenseName):
    # If the license was GPL-2.0-only, it uses the same COPYING file as
    # GPL-2.0-or-later, because the only place the "or later" part is mentioned
    # in the license file is in describing the "or later" system, the actual
    # permission to use later versions must be mentioned separately
    if licenseName == 'GPL-2.0-only':
        licenseName = 'GLP-2.0-or-later'

    if licenseName != NO_LICENSE_CHOICE:
        fileName = '_licenses/' + licenseName + '.txt'
        if not os.path.exists(fileName):
            print('ERROR: missing chosen license file %s!' % fileName)
            sys.exit(1)

        os.rename(fileName, 'COPYING')

    # Delete the others
    licenseFiles = os.listdir('_licenses')
    for file in licenseFiles:
        os.unlink('_licenses/' + file)
    # Delete the directory
    os.rmdir('_licenses')

# This is run *after* the script - the way to implement conditional files is
# to always created them, and then remove them if unneeded.
# https://github.com/cookiecutter/cookiecutter/issues/127
# Placeholders are already replaced, and we only remove files if the placeholder
# was empty, so no need to include in the file name here
CONDITIONAL_FILES = [
    ['{{ cookiecutter.special_page }}', 'src/Special.php'],
    [{{ cookiecutter.has_schema }}, 'sql/tables.json'],
    [{{ cookiecutter.has_schema }}, 'sql/tables-generated.sql'],
    [{{ cookiecutter.has_schema }}, 'sql']
]

# Files with conditions have blank lines to remove
FILES_WITH_BLANK_LINES = ['extension.json', 'i18n/en.json', 'i18n/qqq.json']

def runCleanup():
    for file in FILES_WITH_BLANK_LINES:
        removeBlankLines(file)
    for condition, file in CONDITIONAL_FILES:
        conditionalFile(condition, file)
    processLicense('{{ cookiecutter.license }}')

runCleanup()