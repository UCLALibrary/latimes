# latimes

How to install

1. Download code from this page

        git clone https://github.com/dnoneill/latimes.git

2. Download elasticsearch from https://www.elastic.co/downloads/past-releases/elasticsearch-1-7-3

3. Go into latimes directory

        cd latimes

4. Install requirements
  
        pip install -r requirements
        
5. Start Elasticsearch

        cd elasticsearch/bin
        ./elasticsearch

6. Build search index

        cd latimes
        python manage.py rebuild_index
        
7. Run application

        python manage.py runserver


       
   

