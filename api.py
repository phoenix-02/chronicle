import datetime
from flask import jsonify
from flask_restful import Resource, Api
from app import db
from app.models import Chronicle, Event
from app import app

api = Api(app)


class Main(Resource):
    def get(self,n=20):
        # hardcoded first chronic
        chronicle = db.session.query(Chronicle).first().serialize
        start_date = chronicle['max_timestamp'] - datetime.timedelta(days=n)
        end_date = chronicle['max_timestamp']
        events = db.session.query(Event).filter(Event.aircraft == chronicle['source']).all()
        chronicle['chronicle_events'] = [
            1 if start_date <= event.datetime < chronicle['max_timestamp'] else 0 for event in events
        ]
        chronicle['chronicle_events'].reverse()
        return jsonify(chronicle)


api.add_resource(Main, '/<int:n>')
api.add_resource(Main, '/')

if __name__ == '__main__':
    app.run(debug=True)
