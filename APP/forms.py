from flask import flash
from flask_wtf import FlaskForm
from .models import Uploads
from wtforms import EmailField, FileField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError


class ContactForm(FlaskForm):
    '''
        creates contact form with text fields, email fields and text area field, each with individual validations
    '''
    name = StringField(validators=[DataRequired()])
    email = EmailField(validators=[Email()])
    mail_subject = StringField()
    message = TextAreaField(validators=[DataRequired()])


class UploadForm(FlaskForm):
    '''
            creates contact form with text fields, file upload fields and text area field, each with individual validations
    '''
    name = StringField(validators=[DataRequired()])
    regnumber = StringField(validators=[DataRequired()])
    pdf = FileField(validators=[DataRequired()])
    zip = FileField(validators=[DataRequired()])
    topic = TextAreaField(validators=[DataRequired()])
    description = TextAreaField(validators=[DataRequired()])

    def validate_regnumber(self, reg_number):
        '''
        validates the regnumber field entry again database entries
        :param reg_number: data from
        :return: Reg number already exist
        '''
        reg_no = Uploads.query.filter_by(regNo=reg_number.data).first()
        if reg_no:
            raise ValidationError("Reg Number already exists")


def check_errors(form):
    '''
    checks for errors in forms
    :param form:  a form
    :return: a dictionary of errors if errors were found
    '''
    if form.errors != {}:
        for index, err_msg in enumerate(form.errors.values()):
            flash(f'there was an error: {err_msg[index]}', category="danger")


def check_pdf_filename(pdf_file):
    if pdf_file.filename[-4:] == ".pdf":
        return True
    else:
        flash(message="file not pdf", category="danger")
        return False


def check_zip_filename(zip_file):
    file_formats = [".zip", ".rar"]
    if zip_file.filename[-4:] in file_formats:
        return True
    else:
        flash(message="file not a compressed file", category="danger")
        return False
