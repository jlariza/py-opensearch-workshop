from opensearchpy import OpenSearch
from opensearchpy.helpers.search import Search


class OpenSearchConnector(object):

    def __init__(self, *args, **kwargs):
        self.client = OpenSearch(
            hosts=[{"host": "192.168.64.1", "port": 9200}],
            http_compress=False,
            http_auth=("admin", "admin"),
            use_ssl=True,
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )

    def create_index(self, index_name, index_body):
        response = self.client.indices.create(index_name, body=index_body)
        return response

    def delete_index(self, index_name):
        response = self.client.indices.delete(index_name)
        return response

    def index_document(self, index_name, document, refresh=True):
        response = self.client.index(index=index_name, body=document, refresh=refresh)
        return response

    def delete_document(self, index_name, document_id, refresh=True):
        response = self.client.delete(index=index_name, id=document_id, refresh=refresh)
        return response

    def search(self, index_name, query):
        search = Search(
            using=self.client,
            index=index_name,
        )
        response = search.query(query).execute()
        return response
