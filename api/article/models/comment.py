from ...extensions import db, ma
from datetime import datetime


class Comment(db.Model):
    """The Comment Model."""
    __tablename__ = 'comments'
    id: int = db.Column(db.Integer, primary_key=True)
    author_id: int = db.Column(db.Integer, db.ForeignKey('authors.id'))
    article_id: int = db.Column(db.Integer, db.ForeignKey('articles.id'))
    date: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    
    author = db.relationship("Author", backref='comments')
    article = db.relationship("Article", backref="comments")