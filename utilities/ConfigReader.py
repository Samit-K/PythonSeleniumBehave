from configparser import ConfigParser


def read_configuration(category, key):
    # Reads a configuration value from the config.ini file based on the given category and key
    config = ConfigParser()
    config.read("configurations/config.ini")  # Load the configuration file
    return config.get(category, key)  # Retrieve the value for the specified category and key
