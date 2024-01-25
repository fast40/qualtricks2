from __future__ import annotations

from typing import TYPE_CHECKING
import pathlib
from zipfile import ZipFile
import random

from bson import ObjectId

if TYPE_CHECKING:
    import pymongo

DATA_ROOT_DIR = pathlib.Path('/files')
DATABASE = 'qualtricks'


def get(client: pymongo.MongoClient):
    return client[DATABASE]['datasets'].find()


def create(dataset_name: str, zip_file, client):
    dataset_path = DATA_ROOT_DIR.joinpath(dataset_name)

    if dataset_path.exists():
        raise FileExistsError('Dataset has already been created once.')

    with ZipFile(zip_file) as zf:
        zf.extractall(dataset_path)

    documents = {'dataset_name': dataset_name}

    paths = [path for path in dataset_path.rglob('*') if path.is_file() and path.name[0] != '.']
    random.shuffle(paths)

    for i, path in enumerate(paths):
        documents[str(i + 1)] = str(path.relative_to(DATA_ROOT_DIR))
    
    client[DATABASE]['datasets'].insert_one(documents)
    
  
def get_path(dataset_id: str, loop_number: str, client: pymongo.MongoClient):
    return client[DATABASE]['datasets'].find_one({'_id': ObjectId(dataset_id)}, {'_id': 0})[loop_number]
