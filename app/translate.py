from flask_babel import _


# Returns a placeholder message because live translation is not implemented.
def translate(text, source_language, dest_language):
    return _('Translation not available.')
