from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

from app.write2influx import TrigonometricsWriter


app = Flask(__name__, template_folder='template')
api = Api(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


class SignalGenerator(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('samples', type=int)
        parser.add_argument('amplitude', type=int)
        parser.add_argument('period_duration', type=int)
        args = parser.parse_args()

        app.logger.info('SignalGenerator received the following parameters: %s', str(args))
        app.logger.info('Start writing...')
        writer = TrigonometricsWriter(logger=app.logger)
        writer.write(**args)
        app.logger.info('Done.')

        return {'message': 'SUCCESS'}, 201


api.add_resource(SignalGenerator, '/generator')


if __name__ == '__main__':
    app.run(debug=True)
