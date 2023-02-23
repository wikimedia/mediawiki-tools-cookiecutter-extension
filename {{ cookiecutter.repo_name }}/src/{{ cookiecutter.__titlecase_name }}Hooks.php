<?php

namespace MediaWiki\Extension\{{ cookiecutter.__titlecase_name }};

use Config;
use MediaWiki\Hook\BeforePageDisplayHook;
use OutputPage;
use Skin;

/**
 * General hook handler for {{ cookiecutter.__titlecase_name }}
 *{{ cookiecutter.__license_tag }}
 * @author WikiTeq Team
 * @author {{ cookiecutter.author_name }}
 */
class {{ cookiecutter.__titlecase_name }}Hooks implements BeforePageDisplayHook {

    /** @var Config */
    private $config;

    /**
     * @param Config $config
     */
    public function __construct( Config $config ) {
        // Demonstration of services being injected
        $this->config = $config;
    }

	/**
	 * This hook is called prior to outputting a page.
	 *
	 * @param OutputPage $out
	 * @param Skin $skin
	 * @return void This hook must not abort, it must return no value
	 */
    public function onBeforePageDisplay( $out, $skin ): void {
        if ($this->config->get('ext.{{ cookiecutter.__titlecase_name }}Enabled')) {
            $out->addModule( "ext.{{ cookiecutter.__titlecase_name }}" );
        }
    }
}