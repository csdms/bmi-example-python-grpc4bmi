#!/usr/bin/env python
# Run the `Heat` model through its BMI.
#
# `Heat` models the diffusion of temperature on a uniform rectangular plate with
# Dirichlet boundary conditions. View the model source code and its BMI at
# https://github.com/csdms/bmi-example-python.

import os
import pathlib
import numpy as np

from heat import BmiHeat
from grpc4bmi.bmi_client_docker import BmiClientDocker

DOCKER_IMAGE = "mdpiper/bmi-example-python-grpc4bmi"
BMI_PORT = 55555
REPO_PATH = pathlib.Path("/opt/bmi-example-python")
CONFIG_FILE = REPO_PATH / "examples" / "heat.yaml"


# Create a model instance from the container.
x = BmiClientDocker(image=DOCKER_IMAGE, image_port=BMI_PORT, work_dir=".")

# Show the name of this model.
print(x.get_component_name())

# Start the `Heat` model through its BMI using a configuration file.
x.initialize(CONFIG_FILE)

# Show the input and output variables for the component.
print(x.get_input_var_names())
print(x.get_output_var_names())

# Check the time information for the model.
print("Start time:", x.get_start_time())
print("End time:", x.get_end_time())
print("Current time:", x.get_current_time())
print("Time step:", x.get_time_step())
print("Time units:", x.get_time_units())

# Get the identifier for the grid on which the temperature variable is defined.
grid_id = x.get_var_grid("plate_surface__temperature")
print("Grid id:", grid_id)

# Get the grid attributes.
print("Grid type:", x.get_grid_type(grid_id))
rank = x.get_grid_rank(grid_id)
print("Grid rank:", rank)
shape = np.ndarray(rank, dtype=int)
x.get_grid_shape(grid_id, shape)
print("Grid shape:", shape)
spacing = np.ndarray(rank, dtype=float)
x.get_grid_spacing(grid_id, spacing)
print("Grid spacing:", spacing)

# Through the model's BMI, zero out the initial temperature field, except for an
# impulse near the middle. Note that *set_value* expects a one-dimensional array
# for input.
temperature = np.zeros(shape)
temperature[3, 4] = 100.0
x.set_value("plate_surface__temperature", temperature)

# Check that the temperature field has been updated. Note that *get_value*
# expects a one-dimensional array to receive output.
temperature_flat = np.empty_like(temperature).flatten()
x.get_value("plate_surface__temperature", temperature_flat)
print(temperature_flat.reshape(shape))

# Advance the model by a single time step.
x.update()

# View the new state of the temperature field.
x.get_value("plate_surface__temperature", temperature_flat)
print(temperature_flat.reshape(shape))

# Advance the model to some distant time.
distant_time = 2.0
while x.get_current_time() < distant_time:
    x.update()

# View the final state of the temperature field.
np.set_printoptions(formatter={"float": "{: 5.1f}".format})
x.get_value("plate_surface__temperature", temperature_flat)
print(temperature_flat.reshape(shape))

# Note that temperature isn't conserved on the plate.
print(temperature_flat.sum())

# Stop the model.
x.finalize()

# Stop the container.
del x
