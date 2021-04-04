# news_crud

Django Rest Framework project that implements CRUD functionallity.

Code formatted using:
- [Black](https://github.com/psf/black)
- Flake8 
- pyright

**Postman Documentation:**

https://documenter.getpostman.com/view/14798392/TzCQa5z8

**Deployed Heroku application:**

https://django-main-news-crud.herokuapp.com/

For application functionality visit:

https://django-main-news-crud.herokuapp.com/api/

**Run on Docker:**

``` 
docker-compose run web python news/manage.py migrate   
docker-compose up
```

After docker-compose up go to http://0.0.0.0:8000/ or use link to Heroku project. 
