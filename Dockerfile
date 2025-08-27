# A grpc4bmi server for the bmi-example-python `Heat` model.
FROM csdms/grpc4bmi:0.3.0

LABEL author="Mark Piper"
LABEL email="mark.piper@colorado.edu"

RUN pip install grpc4bmi

WORKDIR /opt
ENV BMI_PORT=55555
ENTRYPOINT ["run-bmi-server", "--name", "heat.BmiHeat"]
EXPOSE ${BMI_PORT}
