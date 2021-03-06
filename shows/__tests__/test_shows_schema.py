from django.test import TestCase
from graphene.test import Client
from model_bakery import baker

from api import schema
from fields import VISIBILITY_PRIVATE, VISIBILITY_PUBLIC


class ShowsSchemaTest(TestCase):
    def test_list_shows_includes_visible(self):
        show_type = baker.make(
            "shows.ShowType",
            name="Představení",
            description="Testovací typ představení",
            visibility=VISIBILITY_PUBLIC,
        )
        show_location = baker.make(
            "locations.Location",
            name="Divadlo Bez Hranic",
            description="Location description",
            visibility=VISIBILITY_PUBLIC,
        )
        baker.make(
            "shows.Show",
            name="Test show",
            description="Test show description",
            location=show_location,
            visibility=VISIBILITY_PUBLIC,
            show_type=show_type,
        )

        client = Client(schema.PUBLIC)
        result = client.execute("""{ showList { name } }""")
        self.assertEqual(result, {"data": {"showList": [{"name": "Test show",},],},})

    def test_list_shows_excludes_private(self):
        show_type = baker.make(
            "shows.ShowType",
            name="Představení",
            description="Testovací typ představení",
            visibility=VISIBILITY_PUBLIC,
        )
        show_location = baker.make(
            "locations.Location",
            name="Divadlo Bez Hranic",
            description="Location description",
            visibility=VISIBILITY_PUBLIC,
        )
        baker.make(
            "shows.Show",
            name="Test show",
            description="Test show description",
            location=show_location,
            visibility=VISIBILITY_PRIVATE,
            show_type=show_type,
        )

        client = Client(schema.PUBLIC)
        result = client.execute("""{ showList { name } }""")
        self.assertEqual(result, {"data": {"showList": [],},})
