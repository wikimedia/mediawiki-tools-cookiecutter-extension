<?php

namespace MediaWiki\Extension\{{ cookiecutter.__titlecase_name }};

use DatabaseUpdater;
use MediaWiki\Installer\Hook\LoadExtensionSchemaUpdatesHook;

/**
 * Hook handler for LoadExtensionSchemaUpdates hook
 * 
 * Needs to be separate from the main hooks because LoadExtensionSchemaUpdates
 * cannot have services injected.
 *{{ cookiecutter.__license_tag }}
 * @author WikiTeq Team
 * @author {{ cookiecutter.author_name }}
 */
class SchemaHooks implements LoadExtensionSchemaUpdates {

	/**
	 * @param DatabaseUpdater $updater
	 */
	public function onLoadExtensionSchemaUpdates( $updater ) {
        $dir = dirname( __DIR__ ) . '/sql/';

        // TODO: actually create the schema, generate the table files, and
        // call addExtensionTable(), etc. - for now this just returns so that
        // we can still install the extension
	}
}