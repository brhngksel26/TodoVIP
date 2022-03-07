from dataclasses import field, fields
import graphene
from graphene_django import DjangoObjectType
from todoApi.models import Todo,MissionGroups,Members,Mission

class TodoSchema(DjangoObjectType):

    class Meta:
        model = Todo
        fields = "__all__" #("created_user","title")


class MissionGroupsSchema(DjangoObjectType):

    class Meta:
        model = MissionGroups
        fields = "__all__" #("title")


class MembersSchema(DjangoObjectType):

    class Meta:
        model = Members
        fields = "__all__" #("member","role","title")


class MissionSchema(DjangoObjectType):

    class Meta:
        model = Mission
        fields = "__all__" #("todo","member","title","description","orderOfImportant","startDate","finishDate","complated")


class Query(graphene.ObjectType):

    all_todo = graphene.List(TodoSchema)
    all_mission_groups = graphene.List(MissionGroupsSchema)
    all_members = graphene.List(MembersSchema)
    all_mission = graphene.List(MissionSchema)

    def resolve_all_todo(self, info, **kwargs):
        try:
            return Todo.objects.all()
        except Todo.DoesNotExist:
            return None

    def resolve_all_mission_groups(self, info, **kwargs):
        try:
            return MissionGroups.objects.all()
        except MissionGroups.DoesNotExist:
            return None
        

    def resolve_all_members(self, info, **kwargs):
        try:            
            return Members.objects.all()
        except Members.DoesNotExist:
            return None
        

    def resolve_all_mission(self, info, **kwargs):
        try:            
            return Mission.objects.all()
        except Mission.DoesNotExist:
            return None
        


schema = graphene.Schema(query=Query)



