<?php

namespace MediaWiki\Extension\{{ cookiecutter.__titlecase_name }};

use SpecialPage;

/**
 * Special page for {{ cookiecutter.__titlecase_name }}
 *{{ cookiecutter.__license_tag }}
 * @author WikiTeq Team
 * @author {{ cookiecutter.author_name }}
 */
class Special{{ cookiecutter.__special_page_name }} extends SpecialPage {

    public function __construct() {
        parent::__construct( '{{ cookiecutter.__special_page_name }}' );
    }

    /** @param string|null $subpage */
    public function execute( $subpage ) {
        parent::execute( $subpage );

        $out->addWikiMsg( '{{ cookiecutter.__sp_i18n_prefix }}-intro' );
    }
}