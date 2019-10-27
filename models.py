from app import db


class Path(db.Model):
    __tablename__ = 'paths'
    id = db.Column(db.Integer, primary_key=True)
    svg = db.Column(db.Text, nullable=False)
    zoom = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Path %r>' % self.id

    def __init__(self, svg, zoom, lat, lng):
        self.svg = svg
        self.zoom = zoom
        self.lat = lat
        self.lng = lng

    def serialize(self):
        return {
            'id': self.id,
            'svg': self.svg,
            'zoom': self.zoom,
            'lat': self.lat,
            'lng': self.lng
        }
