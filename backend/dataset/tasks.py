import traceback
from celery import shared_task, states
from tablib import Dataset
from base64 import b64decode

from .resources import RESOURCE_MAP

#### CELERY SHARED TASKS


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    exponential_backoff=2,
    retry_kwargs={
        "max_retries": 5,
        "countdown": 2,
    },
)
def upload_data_to_data_instance(self, dataset_string, pk, dataset_type, content_type):
    """Celery background task to upload the data to the dataset instance through file upload

    Args:
        dataset_string (str): The data to be uploaded in string format
        pk (int): Primary key of the dataset instance
        dataset_type (str): The type of the dataset instance
        content_type (str): The file format of the uploaded file
    """

    # Create a new tablib Dataset and load the data into this dataset
    if content_type in ['xls', 'xlsx']:
        imported_data = Dataset().load(b64decode(dataset_string), format=content_type)
    else:
        imported_data = Dataset().load(dataset_string, format=content_type)

    # Add the instance_id column to all rows in the dataset
    imported_data.append_col([pk] * len(imported_data), header="instance_id")

    # Declare the appropriate resource map based on dataset type
    resource = RESOURCE_MAP[dataset_type]()

    # Import the data into the database and return Success if all checks are passed
    try:
        resource.import_data(imported_data, raise_errors=True)

    # If validation checks fail, raise the Exception
    except Exception as e:
        self.update_state(
            state="FAILURE",
            meta={
                "exc_type": type(e).__name__,
                "exc_message": traceback.format_exc().split("\n"),
            },
        )
        raise e