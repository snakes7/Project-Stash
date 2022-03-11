from APP import db

class Uploads(db.Model):
    '''
    Uploads class which holds the columns and datatype and attributes of each entity (project)
    '''
    id = db.Column(db.Integer(), primary_key=True)
    uploaded_by = db.Column(db.String(), nullable=False)
    regNo = db.Column(db.String(9), unique=True)
    topic = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    pdf = db.Column(db.LargeBinary(), nullable=False)
    pdf_filename = db.Column(db.String(2048), nullable=False)
    zip = db.Column(db.LargeBinary(), nullable=False)
    zip_filename = db.Column(db.String(2048), nullable=False)

    # year =  db.Column(db.String(4),nullable=False)

    def __init__(self, name ,regNo, topic, desc, pdf, pdf_filename, zip, zip_filename):
        self.uploaded_by = name
        self.regNo = regNo
        self.topic=topic
        self.description = desc
        self.pdf = pdf
        self.pdf_filename=pdf_filename
        self.zip = zip
        self.zip_filename=zip_filename

def add_and_commit_to_db(object):
    '''

    :param object: an instance of the Upload class

    '''
    db.session.add(object)
    db.session.commit()

