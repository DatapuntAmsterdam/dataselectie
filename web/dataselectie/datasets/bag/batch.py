import logging

from django.conf import settings

from . import models
from ..generic import index
from . import documents

log = logging.getLogger(__name__)

BAG_DOC_TYPES = (
    documents.NummeraanduidingMeta,
)


class DeleteBagIndexTask(index.DeleteIndexTask):
    index = settings.ELASTIC_INDICES['DS_BAG']
    doc_types = BAG_DOC_TYPES



class IndexBagTask(index.ImportIndexTask):
    name = "index bag data"
    if settings.IN_TEST_MODE:
        queryset = models.Nummeraanduiding.objects. \
            prefetch_related('verblijfsobject').\
            prefetch_related('standplaats').\
            prefetch_related('ligplaats').\
            prefetch_related('openbare_ruimte')
    else:
        queryset = models.Nummeraanduiding.objects. \
            prefetch_related('verblijfsobject').\
            prefetch_related('standplaats').\
            prefetch_related('ligplaats').\
            prefetch_related('openbare_ruimte')

    def convert(self, obj):
        return documents.meta_from_nummeraanduiding(obj)


class BuildIndexBagJob(object):
    name = "Create new search-index for all BAG data from database"

    @staticmethod
    def tasks():
        return [
            DeleteBagIndexTask(),
            IndexBagTask(),
        ]


class DeleteIndexBagJob(object):
    name = "Delete BAG related indexes"

    @staticmethod
    def tasks():
        return [DeleteBagIndexTask()]
