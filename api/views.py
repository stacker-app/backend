from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .serializers import *


class GoalView(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    model = Goal
    queryset = Goal.objects.all()

    def get_queryset(self):
        # Only my Goals
        return Goal.objects. \
            filter(owner=self.request.user)

    # Owner default set
    def perform_create(self, serializer):
        # if done: completed=now
        c = None
        if 'done' in self.request.data :
            c = now()

        serializer.save(owner=self.request.user, completed=c)


class ActionView(viewsets.ModelViewSet):
    serializer_class = ActionSerializer
    queryset = Action.objects.all()
    model = Action

    def get_queryset(self):
        # I <3 native sql
        return Action.objects.raw(
            'SELECT * FROM api_action a WHERE EXISTS(SELECT * FROM api_goal g WHERE g.owner_id = %s AND a.goal_id = g.id)',
            [self.request.user.id]
        )

    def perform_create(self, serializer):
        # SELECT GOAL WHERE USER = CURRENT & ID = request
        my = Goal.objects.filter(owner=self.request.user, id=self.request.data['goal'])
        if not my:
            raise APIException("Goal with id ="+str(self.request.data['goal'])+" doesnt exists!")