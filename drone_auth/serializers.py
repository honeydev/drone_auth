from typing import Dict

from django.db import transaction
from djoser.serializers import User, UserCreateSerializer

from drone_auth import settings


class CreateNotActiveUserSerializer(UserCreateSerializer):
    """Redefine default djoser create user implementation."""

    def perform_create(self, validated_data: Dict[str, str]) -> User:
        """Redefined create user method.

        Include 'CREATE_NOT_ACTIVE_USERS'settings check.
        """
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            send_activation_email = settings.DJOSER.get(
                'SEND_ACTIVATION_EMAIL',
                False,
            )

            create_not_active_users = settings.DJOSER.get(
                'CREATE_NOT_ACTIVE_USERS',
                False,
            )

            if send_activation_email or create_not_active_users:
                user.is_active = False
                user.save(update_fields=['is_active'])

        return user
