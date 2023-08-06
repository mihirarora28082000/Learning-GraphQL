import graphene
from graphene_django import DjangoObjectType
from apps.users.models import User as UserModal


class User(DjangoObjectType):
    class Meta:
        model = UserModal


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info, **kwargs):
        return UserModal.objects.all()


schema = graphene.Schema(query=Query)
