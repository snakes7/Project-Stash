from APP import app
from flask import flash, render_template, redirect, request, send_file, url_for
from .forms import ContactForm, UploadForm, check_errors, check_pdf_filename, check_zip_filename
from io import BytesIO
from .models import Uploads, add_and_commit_to_db


@app.route('/', methods=["GET", "POST"])
def index():

    upload_form = UploadForm()

    # form validations
    if upload_form.validate_on_submit():
        if request.method == "POST":
            pdf_file = request.files['pdf']
            zip_file = request.files['zip']

            # checking if pdf_file and zip_file are pdf and zip files
            if check_pdf_filename(pdf_file) and check_zip_filename(zip_file):

                # instantiating an upload object with required data from form as arguments
                upload = Uploads(name=upload_form.name.data, regNo=upload_form.regnumber.data,
                                 topic=upload_form.topic.data,
                                 desc=upload_form.description.data, pdf=pdf_file.read(), pdf_filename=pdf_file.filename,
                                 zip=zip_file.read(), zip_filename=zip_file.filename)
                try:
                    add_and_commit_to_db(upload)
                    flash(message="Upload Successful", category="success")
                except:
                    flash(message="Upload failed", category="danger")
                return redirect(url_for("index"))

    # checking for other errors in the form
    check_errors(upload_form)
    return render_template("index.html", upload_form=upload_form)


@app.route('/about')
def contact():
    '''
    redirects to contact section of the index page
    :return: index page
    '''
    return redirect(url_for("index", _anchor="contact"))


@app.route('/view-files')
def view_all():
    '''
    Queries the Uploads table in the db
    :return: /view_all route
    '''
    results = Uploads.query.all()
    return render_template("all-files.html", results=results)


@app.route('/search')
def search():
    return render_template("search.html")


@app.route('/download/pdf/<int:id>')
def download_pdf(id):
    '''
        downloads each pdf file
        :param id: gets the id of the file in the database and passes it as a route variable
        :return: A downloadable file with certain id in the database with filename and .pdf extension
        '''
    item = Uploads.query.get_or_404(id)
    return send_file(BytesIO(item.pdf), attachment_filename=item.pdf_filename, as_attachment=True)


@app.route('/download/zip/<int:id>')
def download_zip(id):
    '''
    downloads each zip
    :param id: gets the id of the file in the database and passes it as a route variable
    :return: A downloadable file with certain id in the database with filename and .zip extension
    '''
    item = Uploads.query.get_or_404(id)
    return send_file(BytesIO(item.zip), attachment_filename=item.zip_filename, as_attachment=True)

@app.errorhandler(404)
def page_not_found(e):
    '''
        page not found error handler
    :param e:
    :return: error 404 webpage
    '''
    return render_template("error404.html")

@app.errorhandler(413)
def page_not_found(e):
    '''
        file too large error handler
    :param e:
    :return: error 413 webpage
    '''
    return render_template("error413.html")

download_zip()