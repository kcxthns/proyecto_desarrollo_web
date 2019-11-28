#valida el tipo de archivo
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx', '.txt']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Tipo archivo no soportado')