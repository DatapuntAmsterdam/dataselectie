import logging

from django.conf import settings

from datasets.hr import models
from . import documents
from ..generic import index

log = logging.getLogger(__name__)

HR_DOC_TYPES = (
    documents.VestigingenMeta,
)


class IndexHrTask(index.ImportIndexTask):
    name = "index hr data"
    index = settings.ELASTIC_INDICES['DS_INDEX']

    queryset = models.DataSelectie.objects.filter(bag_numid__isnull=False)

    def convert(self, obj):
        return documents.meta_from_hrdataselectie(obj)


class BuildIndexHrJob(object):
    name = "Create new search-index for all HR data from database"

    @staticmethod
    def tasks():
        return [IndexHrTask()]

