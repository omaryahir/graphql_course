from graphene_django import DjangoObjectType
from notes.models import Note

class NoteType(DjangoObjectType):
    class Meta:
        model = Note
        only_fields = (
            'id',
            'title',
            'body',
            'created_at'
        )
        use_connection = True

    def resolver_is_old(root, *args):
        return root.created_at < (timezone.now() - timezone.timedelta(days=777))
        
