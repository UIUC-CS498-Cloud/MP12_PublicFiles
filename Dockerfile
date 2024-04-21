FROM python:3.6

# Creating Application Source Code Directory
RUN ...

# Setting Home Directory for containers
WORKDIR ...

# Copy src files folder (requirements.txt and classify.py)
COPY ...

# Installing python dependencies
RUN ...

# create directories for models and data
RUN ...
RUN ...

# Preload the data
RUN ...

# Pretrain the models
RUN ...
RUN ...
RUN ...
RUN ...


# Application Environment variables. 
# These variables will be used when you run the image. 
# You will also need to pass corresponding DATASET and TYPE variables from the job yaml files of both free-service and default types of jobs.
ENV APP_ENV development
ENV DATASET mnist
ENV TYPE ff

# Exposing Ports
EXPOSE 5035

# Setting Persistent data
VOLUME ["/app-data"]

# Running Python Application (classify.py)
CMD ...
