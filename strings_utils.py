def convert_strings_to_booleans(config):
    def str_to_bool(s):
        if s.lower() == 'true':
            return True
        elif s.lower() == 'false':
            return False
        return s

    if isinstance(config, dict):
        return {key: convert_strings_to_booleans(value) for key, value in config.items()}
    elif isinstance(config, list):
        return [convert_strings_to_booleans(item) for item in config]
    else:
        return str_to_bool(config)