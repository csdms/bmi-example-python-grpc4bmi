# bmi-example-python-grpc4bmi

Set up a [grpc4bmi](https://grpc4bmi.readthedocs.io) server
to run a containerized version
of the [Basic Model Interface](https://bmi.readthedocs.io)
[Python example](https://github.com/csdms/bmi-example-python).

## Build

Build the server image locally with:
```
docker build --tag bmi-example-python-grpc4bmi .
```
The image is built on the [csdms/bmi-example-python](https://hub.docker.com/r/csdms/bmi-example-python) image.
The OS is Linux/Ubuntu.
`conda` and `mamba` are installed in `CONDA_DIR=opt/conda`,
and the *base* environment is activated,
The grpc4bmi Python server,
as well as the Python BMI specification and example
(consisting of the *Heat* model and a BMI implementation, *BmiHeat*)
are installed into it.

## Run

Use the grpc4bmi [Docker client](https://grpc4bmi.readthedocs.io/en/latest/container/usage.html#docker)
to access the BMI methods of the containerized model.
Install grpc4bmi with *pip*:
```
pip install grpc4bmi
```
Then, in a Python session, access the *Heat* model in the image built above with:
```python
from grpc4bmi.bmi_client_docker import BmiClientDocker

IMAGE_NAME = "bmi-example-python-grpc4bmi"
m = BmiClientDocker(image=IMAGE_NAME, image_port=55555, work_dir=".")
m.get_component_name()

del m  # stop container cleanly
```

If the image isn't found locally, it's pulled from Docker Hub
(e.g., try substituting `IMAGE_NAME="csdms/bmi-example-python-grpc4bmi"` above).

For a more in-depth example of running the *Heat* model from grpc4bmi,
see the [examples](./examples) directory.

## Developer notes

A versioned, multiplatform image built from this repository is hosted on Docker Hub
at [csdms/bmi-example-python-grpc4bmi](https://hub.docker.com/r/csdms/bmi-example-python-grpc4bmi).
When this repository is tagged,
an image is automatically built and pushed to Docker Hub
by the [release](./.github/workflows/release.yml) CI workflow.
To manually build and push an update, run:
```
docker buildx build --platform linux/amd64,linux/arm64 -t csdms/bmi-example-python-grpc4bmi:latest --push .
```
A user can pull this image from Docker Hub with:
```
docker pull csdms/bmi-example-python-grpc4bmi
```
optionally with the `latest` tag or with a version tag.

## What are the Basic Model Interface and grpc4bmi?

The Basic Model Interface (BMI) is a set of functions for querying, modifying, running, and coupling models.
Learn more at https://bmi.readthedocs.io/.

grpc4bmi is a [gRPC](https://grpc.io/) wrapper for a model with a BMI.
Learn more at https://grpc4bmi.readthedocs.io/.

## Acknowledgment

This work is supported by the U.S. National Science Foundation under Award No. [2103878](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2103878), *Frameworks: Collaborative Research: Integrative Cyberinfrastructure for Next-Generation Modeling Science*.
