from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from openbook_auth.models import User
from openbook_notifications.models.notification import Notification


class ConnectionRequestNotification(models.Model):
    notification = GenericRelation(Notification)
    connection_requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    @classmethod
    def create_connection_request_notification(cls, connection_requester_id, owner_id):
        connection_request_notification = cls.objects.create(connection_requester_id=connection_requester_id)
        return Notification.create_notification(type=Notification.CONNECTION_REQUEST,
                                                content_object=connection_request_notification,
                                                owner_id=owner_id)

    @classmethod
    def delete_connection_request_notification_for_users_with_ids(cls, user_a_id, user_b_id):
        notification_query = Q(connection_requester_id=user_a_id, notification__owner_id=user_b_id)

        notification_query.add(Q(connection_requester_id=user_b_id, notification__owner_id=user_a_id), Q.OR)

        cls.objects.filter(notification_query).delete()


@receiver(pre_delete, sender=ConnectionRequestNotification, dispatch_uid='connection_request_delete_cleanup')
def connection_request_notification_pre_delete(sender, instance, using, **kwargs):
    Notification.objects.filter(notification_type=Notification.CONNECTION_REQUEST, object_id=instance.pk).delete()
