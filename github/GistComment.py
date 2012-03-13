from GithubObject import *

from NamedUser import NamedUser

GistComment = GithubObject(
    "GistComment",
    BaseUrl( lambda obj: "/gists/comments/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "id", "url", "body", "created_at",
        "updated_at",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( [ "body" ], [] ),
    Deletable(),
)
