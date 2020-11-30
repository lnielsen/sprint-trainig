"""Small example app

Running:

    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run

Testing:

    curl -X GET -H "Accept: text/plain" http://127.0.0.1:5000/records/
    curl -X GET -H "Accept: application/json" http://127.0.0.1:5000/records/
    curl -X GET -H "Accept: text/plain" http://127.0.0.1:5000/records/1
"""

from flask import Flask
from flask_resources.context import resource_requestctx
from flask_resources.resources import CollectionResource, ResourceConfig
from flask_resources.responses import Response
from flask_resources.serializers import JSONSerializer, SerializerMixin

# Initialize the Flask application
app = Flask(__name__)


# Create a serializer
class PlainTextSerializer(SerializerMixin):

    def serialize_object(self, obj):
        return obj['id']

    def serialize_object_list(self, obj_list):

        return ', '.join([d['id'] for d in obj_list])


# Create the REST API Resource
class MyResourceConfig(ResourceConfig):
    item_route = "/records/<id>"
    list_route = "/records/"

    response_handlers = {
        "application/json": Response(JSONSerializer()),
        "text/plain": Response(PlainTextSerializer())
    }


class MyResource(CollectionResource):
    db = {
        '1': 'an',
        '2': 'flask-resource',
        '3': 'example',
    }

    def search(self):
        """Search."""
        query = resource_requestctx.url_args.get("q", [""])[0]
        resp = []
        for key, value in self.db.items():
            if query in key or query in value:
                resp.append({"id": key, "content": value})

        return resp, 200

    def create(self):
        """Create."""
        obj = resource_requestctx.request_content
        self.db[obj["id"]] = obj["content"]
        return self.db, 201

    def read(self):
        """Read."""
        _id = resource_requestctx.route["id"]
        return {"id": _id, "content": self.db[_id]}, 200

    def delete(self):
        """Delete."""
        _id = resource_requestctx.route["id"]
        if _id in self.db:
            del self.db[_id]
        return {}, 200


# Register the resource
blueprint = MyResource(config=MyResourceConfig).as_blueprint("myresource")
app.register_blueprint(blueprint)
