

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    if not data.get('name'):
        flash('Name is required!')
        return redirect(url_for('index'))
    # Continue with normal processing of the form data
