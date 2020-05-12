def handle_uploaded_file(f):  
    with open(os.path.join(BASE_DIR, 'home/site/wwwroot/static/upload/'+f.name), 'wb+')) as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  