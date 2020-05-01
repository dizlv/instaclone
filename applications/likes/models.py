from extensions.database import db


class Like(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
    )

    photo_id = db.Column(
        db.Integer,
        db.ForeignKey('photo.id'),
        nullable=False,
    )
