from flask import Flask, request
from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy



app = Flask(__name__)
Swagger(app)
CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}


@app.route('/preprocess', methods=['POST'])
def date_preprocess():
    """
    Micro Service This API is made with Flask, Flasgger and Nameko
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          properties:
            studyUID:
              type: string
    responses:
      200:
        description: Please wait the calculation, you'll receive an email with results
    """
    studyuid = request.json.get('studyUID')
    msg = "Please wait the calculation..."

    with ClusterRpcProxy(CONFIG) as rpc:
        
        print("receiving the request studyUID: %s" % studyuid)
        result = rpc.service_dispatch.dispatching_load.call_async(studyuid)
        print("put the requet into queue, result %s" % studyuid) 
        return msg, 200


@app.route('/')
def main():
    return 'helo world'
    

if __name__ == "__main__":
    app.run(debug=True)
