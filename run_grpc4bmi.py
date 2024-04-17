from grpc4bmi.bmi_client_docker import BmiClientDocker


m = BmiClientDocker(image='mdpiper/bmi-example-python-grpc4bmi', image_port=55555, work_dir=".")
m.get_component_name()
del m  # stop container
