from flask import current_app

def add_to_index(index, model):
    # Indexes a model's searchable fields into Elasticsearch. No-ops if Elasticsearch is not configured.
    if not current_app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, id=model.id, document=payload)

def remove_from_index(index, model):
    # Deletes a model's document from the Elasticsearch index by its ID.
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, id=model.id)

def query_index(index, query, page, per_page):
    # Searches an Elasticsearch index with a multi-field match query and returns a paginated list of IDs and total hit count.
    if not current_app.elasticsearch:
        return [], 0
    search = current_app.elasticsearch.search(
        index=index,
        query={'multi_match' : {'query': query, 'fields': ['*']}},
        from_=(page - 1) * per_page,
        size=per_page
    )
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']['value']