import connexion
import six

from swagger_server.models.trainer import Trainer  # noqa: E501
from swagger_server import util


def create_trainer(body):  # noqa: E501
    print('create trainer')
    """Create a new trainer.

     # noqa: E501

    :param body: A trainer record with required information
    :type body: dict | bytes

    :rtype: Trainer
    """
    if connexion.request.is_json:
        body = Trainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_trainer(id):  # noqa: E501
    print('get trainer')
    """Get a trainer by ID.

     # noqa: E501

    :param id: The ID of the requested trainer record
    :type id: str

    :rtype: Trainer
    """
    return 'do some magic!'
