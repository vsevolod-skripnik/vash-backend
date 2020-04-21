from rest_framework.test import APIClient


class UserApiClient(APIClient):
    """DRF testing client with user attribute."""

    def force_authenticate(self, user=None, token=None):
        """Default `force_authenticate` with monkey-patched `user` attribute"""
        self.user = user
        return super().force_authenticate(user=user, token=token)
