# A grpc4bmi server for the bmi-example-python `Heat` model.
FROM csdms/grpc4bmi:0.3.0

LABEL org.opencontainers.image.authors="Mark Piper <mark.piper@colorado.edu>"
LABEL org.opencontainers.image.source="https://github.com/csdms/bmi-example-python-grpc4bmi"
LABEL org.opencontainers.image.url="https://hub.docker.com/r/csdms/bmi-example-python-grpc4bmi"
LABEL org.opencontainers.image.vendor="CSDMS"

RUN pip install grpc4bmi && \
    pip cache purge

WORKDIR /opt
ENV BMI_PORT=55555
ENTRYPOINT ["run-bmi-server", "--name", "heat.BmiHeat"]
EXPOSE ${BMI_PORT}
