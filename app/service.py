import csv
import yaml
from yaml import Loader
from app.models import Category

formats = {
    "csv": "csv",
    "yaml": "yaml"
}


def load_data_csv(data):
    return csv.DictReader(data, delimiter=";")


def load_db(data):
    Category.objects.bulk_create([Category(name=cat["category"]) for cat in data], ignore_conflicts=True)


def load_data_yaml(data):
    return yaml.load(data, Loader=Loader)


def load_db_yaml(data):
    print(data["categories"])
    Category.objects.bulk_create([Category(name=cat["name"]) for cat in data["categories"]], ignore_conflicts=True)



def import_data_all(data_all, format):
    if format not in formats:
        raise NotImplementedError(f"{format} not supported")
    elif format == "csv":
        data = load_data_csv(data_all)
        load_db(data)
    else:
        data = load_data_yaml(data_all)
        load_db_yaml(data)


