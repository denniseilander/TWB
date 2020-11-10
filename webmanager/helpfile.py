help_file = {
    'server': 'Configure the world the bot should play on',
    'server.server': 'The server endpoint to use (the world)',
    'server.endpoint': 'Endpoint server to use (the full url)',
    'server.server_on_twplus': 'Is the server listed on twplus.org?',
    'reporting': 'Enable advanced reporting features',
    'reporting.enabled': 'Enable the reporting feature',
    'reporting.connection_string': 'Could be of type file://filename or mysql://user:password@host:port/database_name',
    'bot': 'Set global bot configuration variables',
    'bot.active_hours': 'The hours when the bot should use active_delay (this does not impact attack timings)',
    'bot.delay_factor': 'Delay factor to use 5-7seconds * delay factor (very low factors will probably cause ban)',
    'bot.active_delay': 'Delay in seconds to use in bot active times',
    'bot.inactive_delay': 'Delay in seconds to use in bot inactive times',
    'bot.inactive_still_active': 'Inactive to stop the bot from running during inactive times',
    'bot.add_new_villages': 'Automatically add the default village config to newly conquered villages',
    'bot.village_name_template': 'Template to use for new villages, use {num} to set the config index as name',
    'bot.village_name_number_length': 'The number length, lower will be prefixed with zeroes',
    'bot.auto_set_village_names': 'Automatically set villages names',
    'bot.user_agent': 'Set this to the browser agent your session is using (otherwise could cause ban)',
    'building.manage_buildings': 'Automatically manage buildings',
    'building': 'The automatic creation of buildings',
    'building.default': 'The default template to use, village configs override this variable',
    'building.max_lookahead': 'The max amount of items in queue to check before stopping',
    'building.max_queued_items': 'Max amount of queued items, default: 2 premium: 5',
    'units': 'Enable automatic recruitment of units',
    'units.recruit': 'Automatically recruit units',
    'units.upgrade': 'Automatically upgrade units (only for level 1-3, 1-10 smith systems)',
    'units.default': 'The default template for unit creation (templates/troops)',
    'units.batch_size': 'The amount of units to attempt to create in a single run, increase this in late-game',
    'units.manage_defence': 'Manage defence between villages (experimental)',
    'units.remove_manual_queued': 'Remove manual queued recruitment entries',
    'units.randomize_unit_queue': 'Randomize unit queue, allows a more wide variety in units',
    'farms': 'Automatic farming of nearby (barbarian) villages',
    'farms.farm': 'Enable automatic farming',
    'farms.min_points': 'The minimum points of villages to attack (also checks custom_farms)',
    'farms.max_points': 'The maximum points of villages to attack (also checks custom_farms)',
    'farms.find_player_owned': 'Automatically attacks all player owned villages (dangerous)',
    'farms.search_radius': 'Max radius of villages to attack (fields)',
    'farms.default_away_time': 'Default time in seconds to sleep before attacking a village again',
    'farms.full_loot_away_time': 'Away time for villages with high resource gain',
    'farms.low_loot_away_time': 'Away time for villages with low resource gain',
    'farms.max_farms': 'The amount of nearby villages to check',
    'farms.attack_higher_points': 'If enabled villages with higher points than the current one will automatically be ignored',
    'farms.force_scout_if_available': 'Will only attack villages that have either been attacked before or it will automatically scout them',
    'market': 'Automatic management of market trading',
    'market.auto_trade': 'Enable automated trading',
    'market.max_trade_duration': 'Max duration of trades (hours)',
    'market.auto_remove': 'Automatically removes existing or expired trades',
    'market.trade_multiplier': 'Set to true if the world supports uneven trade ratios',
    'market.trade_multiplier_value': 'Multiplier value (lower is more gain)',
    'market.trade_max_per_hour': 'The amount of trades the bot can do in 1 hour',
    'world.knight_enabled': 'The world has knights enabled',
    'world.flags_enabled': 'Allows automatic management of flags (upgrading and defence)',
    'world.quests_enabled': 'World has quests enabled (bot will automatically finish them)',
    'world.trade_for_premium': 'World has the premium market enabled (doing this too much could result in ban)',
    'world.archers_enabled': 'Are archers / marchers enabled on the world',
    'world.building_destruction_enabled': 'Are rams / catpults enabled on the world',
    'village_template': 'The default template for villages to use',
    'village.building': 'Override build template',
    'village.units': 'Override recruitment / farm template',
    'village.managed': 'The village should be managed by the bot',
    'village.scout_first': 'The village should scout villages before farming',
    'village.additional_farms': 'List of villages to include in the farming process (does not require find_player_owned to be active)',
    'village.prioritize_building': 'Do not recruit if the builder does not have enough resources',
    'village.prioritize_snob': 'Do not recruit if the snob does not have enough resources',
    'village.trade_for_premium': 'Trade left-over resources for premium points (requires the global option to be enabled)',
    'village.gather_enabled': 'Uses left-over units to gather additional resources if the option is enabled on the world',
    'village.gather_selection': 'The gather operation to preform (they have to be unlocked first)',
    'village.snobs': 'The amount of snobs to create in the current village',
    'village.evacuate_fragile_units_on_attack': 'Automatically evacuate fragile units (axe, snob) to nearby safe villages in case of an attack',
    'village.support_others': 'Allows the sending of automatic support',
    'village.support_others_factor': 'Factor of units to use in support operation (only defensive ones)',
    'village.support_others_max_villages': 'The max amount of villages to send support to (total 2 * 25% of troops)',
    'village.request_support_on_attack': 'Allows automatic requesting of support units'
}
buildings = ["main", "barracks", "stable", "watchtower", "smith", "garage", "place", "statue", "market", "wood", "stone", "iron", "farm", "hide", "wall", "snob", "church"]