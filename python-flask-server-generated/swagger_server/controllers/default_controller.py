import connexion
import six
import pymongo
import os

from swagger_server.models.trainer import Trainer  # noqa: E501
from swagger_server import util

from bson.objectid import ObjectId

conn_str = os.environ["MONGOSERVER"]
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.cgdb
trainers = db.trainers

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")


def create_trainer(body):  # noqa: E501
    """Create a new trainer.

     # noqa: E501

    :param body: A trainer record with required information
    :type body: dict | bytes

    :rtype: Trainer
    """
    if connexion.request.is_json:
        trainer_id = trainers.insert_one(body).inserted_id
        body["id"] = str(trainer_id)
        del body["_id"]
        return body
    return "Badly formed request."


def get_trainer(id_):  # noqa: E501
    """Get a trainer by ID.

     # noqa: E501

    :param id: The ID of the requested trainer record
    :type id: str

    :rtype: Trainer
    """
    trainer = trainers.find_one({"_id": ObjectId(id_)})
    trainer["id"] = id_
    del trainer["_id"]
    return trainer
