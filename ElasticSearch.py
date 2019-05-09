#!/home/work/bin/python
# -*-coding:utf8-*-

from elasticsearch import Elasticsearch


class ESSearch():
    def __init__(self, question, top_num=5):
        self.top_num = top_num
        self.es = Elasticsearch(hosts=["localhost:9200"], timeout=500)
        self.question = question
        self.query_body = {
            "query": {
                # "match": {
                #     "content": self.question,
                # }
                "bool": {
                    "must": {
                        "match": {
                            "content": self.question
                        }
                    },
                    "should": {
                        "match": {
                            "title.shingles": self.question
                        }
                    }
                }
            }
        }

    def search(self):
        res = self.es.search(index='question', body=self.query_body, size=self.top_num)
        if len(res['hits']['hits']) == 0:
            return

        return res['hits']['hits'][0]['_source']['content']


if __name__ == '__main__':
    result = ESSearch('1班化学成绩倒数第一的学生?').search()
    print(result)