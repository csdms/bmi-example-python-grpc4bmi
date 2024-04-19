# Set up a grpc4bmi server to run the Python BMI example.
FROM mdpiper/bmi-example-python:0.3

LABEL author="Mark Piper"
LABEL email="mark.piper@colorado.edu"

RUN pip install grpc4bmi

WORKDIR /opt
ENV BMI_PORT=55555
ENTRYPOINT ["run-bmi-server", "--name", "heat.BmiHeat"]
EXPOSE ${BMI_PORT}
