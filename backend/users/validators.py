from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_username(username):
    """Валидация имени пользователя."""
    if username == 'me' or username == 'admin' or username == 'support':
        raise ValidationError(
            f'Использовать "{username}" в качестве username запрещено.'
        )
    regex_validator = RegexValidator(
        regex=r'^[\w.@+$-]+\Z',
        message='Разрешены только буквы, цифры и @/./+/-/_.'
    )
    regex_validator(username)
