

class ConfigurationError(Exception):
    """Base exception for all configuration-related errors."""
    pass

class ValidationError(ConfigurationError):
    """Raised when config values fail validation"""
    pass

class EmptyFieldError(ValidationError):
    """Raised when a required field is empty."""
    pass

class InvalidValueError(ValidationError):
    """Raised when a value is invalid"""

class FileError(ConfigurationError):
    """Raised foe config file problems."""
    pass

class ConfigNotFoundError(FileError):
    """Raised when config file doesn't exist"""
    pass

class WrongFileTypeError(FileError):
    """Raised when file has wrong extension/format"""
    pass
