from chalice import Blueprint

api = Blueprint(__name__)

@api.route('/api-test/{name}')
def api_test_get(name):
  return {'body' : name}