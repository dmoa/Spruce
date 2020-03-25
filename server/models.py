from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app import db

document_editors = db.Table("document_editor",
                            db.Column("document_id", db.Integer, db.ForeignKey("document.id")),
                            db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
                            )

folder_editors = db.Table("folder_editor",
                          db.Column("folder_id", db.Integer, db.ForeignKey("folder.id")),
                          db.Column("user_id", db.Integer, db.ForeignKey("user.id")))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    document_editorships = db.relationship("Document", lazy="subquery", secondary=document_editors,
                                           backref=db.backref("documents", lazy=True))
    folder_editorships = db.relationship("Folder", lazy="subquery", secondary=folder_editors,
                                         backref=db.backref("folders", lazy=True))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey("folder.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
