From python:3
ENV MONGO_DB_USERNAME=admin 
ENV MONGO_DB_PWD=password
RUN mkdir -p /home/project
RUN python -m pip install pymongo
COPY . /home/project
CMD ["pip3 install","pymongo"]
CMD ["python","/home/project/main_code.py"]