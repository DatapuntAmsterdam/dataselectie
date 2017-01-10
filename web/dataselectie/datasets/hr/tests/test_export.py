# Packages
from django.conf import settings
from django.core.management import call_command
from django.test import Client, TestCase
from elasticsearch import Elasticsearch
# Project
from datasets.bag.tests import fixture_utils


class ESTestCase(TestCase):
    """
    TestCase for using with elastic search to reset the elastic index
    """
    @classmethod
    def rebuild_elastic_index(cls):
        """
        Rebuild the elastic search index for tests
        """
        es = Elasticsearch(hosts=settings.ELASTIC_SEARCH_HOSTS)
        call_command('elastic_indices', '--recreate', verbosity=0, interactive=False)
        call_command('elastic_indices', '--build', verbosity=0, interactive=False)
        es.cluster.health(wait_for_status='yellow',
                          wait_for_active_shards=0,
                          timeout="320s")


class DataselectieExportTest(ESTestCase):

    @classmethod
    def setUpTestData(cls):
        super(ESTestCase, cls).setUpTestData()
        fixture_utils.create_nummeraanduiding_fixtures()
        cls.rebuild_elastic_index()

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_complete_export_hr(self):
        response = self.client.get('/dataselectie/hr/export/')
        # assert that response st.values()[:self.preview_size]atus is 200
        self.assertEqual(response.status_code, 200)

        res = (b''.join(response.streaming_content)).decode('utf-8').strip()
        res = res.split('\r\n')
        # 5 lines: headers + 4 items
        self.assertEqual(len(res), 5)
        row2 = res[2].split(';')

        self.assertEqual(len(row2), 32)
        checkvalues = ('Delflandplein', '15', 'C', '', '1012AB', 'Amsterdam', 'Centrum', 'A', '', '',
                       'Burgwallen-Nieuwe Zijde', 'A01', 'Hemelrijk', 'Delflandplein', 'A01b', '', '',
                       '0363000000000004', '', '', '0363000000000111', '', '', '50326457', 'Golf 10 V.O.F.',
                       '000000000809', '4639', 'handel, vervoer, opslag', '',
                       'groothandel (verkoop aan andere ondernemingen, niet zelf vervaardigd)',
                       'Van Puffelen Vennoot', '')

        for idx, val in enumerate(row2):
            self.assertEqual(row2[idx], checkvalues[idx])
