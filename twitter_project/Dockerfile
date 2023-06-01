FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip 


WORKDIR /twitter_project

COPY requirements.txt requirements.txt

RUN apt-get install -y libpq-dev


RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r /twitter_project/requirements.txt && \
    rm -rf /root/.cache
    

COPY . .


#CMD ["waitress-serve", "--port=80", "--call", "app:create_app"]

# Start the Flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"] 
#remove --post=80 for local run