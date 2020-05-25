from flask import render_template
from app import app

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    function to render the 404 error page
    '''
    return render_template('fourOwfour.html')
