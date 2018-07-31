from google.cloud import bigquery
import datetime


class BQReader(object):
    def __init__(self, PROJECT_ID):
        self.client = bigquery.Client(project=PROJECT_ID)
        self.path = 'bq/query/read_test_data.sql'

    def _read_sql(self):
        with open(self.path) as f:
            query = f.read()
        return query

    def _run_query(self, query):
        return self.client.query(query, location='US')  # API request - starts the query

    @staticmethod
    def _to_json_stream(query_job):
        result = ""
        for row in query_job:
            fields = row._xxx_field_to_index.keys()
            vals = row._xxx_values
            row_formatted_js = {}
            for (field, val) in zip(fields, vals):
                row_formatted_js.update({field: parse_datetime(val)})
            result += str(row_formatted_js)
        return result

    def output(self):
        query = self._read_sql()
        job = self._run_query(query)
        result = self._to_json_stream(job)
        print(result)


def parse_datetime(val):
    if isinstance(val, datetime.date):
        return val.strftime('%Y-%m-%d')
    elif isinstance(val, datetime.datetime):
        return val.strftime('%Y-%m-%d\t%H%M%S')
    return val
