# bmi-example-python-grpc4bmi

Set up a [grpc4bmi](https://grpc4bmi.readthedocs.io) server
to run a containerized version
of the [Basic Model Interface](https://bmi.readthedocs.io)
[Python example](https://github.com/csdms/bmi-example-python).

## Build

Build this example locally with:
```
docker build --tag bmi-example-python-grpc4bmi .
```
The image is built on the [mdpiper/bmi-example-python](https://hub.docker.com/r/mdpiper/bmi-example-python) base image.
The OS is Linux/Ubuntu.
`conda` and `mamba` are installed in `opt/conda`.
The *base* environment is activated,
and the Python BMI example is installed into it.

## Run

Use the grpc4bmi [Docker client](https://grpc4bmi.readthedocs.io/en/latest/container/usage.html#docker)
to access the BMI methods of the containerized model.
For example, in a Python session, access the *Heat* model in the image built above with:
```python
from grpc4bmi.bmi_client_docker import BmiClientDocker


m = BmiClientDocker(image='bmi-example-python-grpc4bmi', image_port=55555, work_dir=".")
m.get_component_name()

del m  # stop container cleanly
```

If the image isn't found locally, it's pulled from Docker Hub
(e.g., if you haven't already pulled it, try the `mdpiper/bmi-example-python-grpc4bmi` image from Docker Hub instead).

## Developer notes

A versioned, multiplatform image built from this repository is hosted on Docker Hub
at [mdpiper/bmi-example-python-grpc4bmi](https://hub.docker.com/r/mdpiper/bmi-example-python-grpc4bmi).
To tag, build, and push an update, run:
```
docker buildx build --platform linux/amd64,linux/arm64 -t mdpiper/bmi-example-python-grpc4bmi:<tagname> --push .
```
where `<tagname>` is, e.g., `0.2` or `latest`.

A user can pull this image from Docker Hub with:
```
docker pull mdpiper/bmi-example-python-grpc4bmi
```
