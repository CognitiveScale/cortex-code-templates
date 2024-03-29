"""
Copyright (c) 2021. Cognitive Scale Inc. All rights reserved.

Licensed under CognitiveScale Template/Example Code [License](https://github.com/CognitiveScale/cortex-code-templates/blob/main/LICENSE.md)
"""

from cortex import Cortex
from cortex.experiment import Experiment
from fastapi import FastAPI

app = FastAPI()


@app.post('/invoke')
def run(request_body: dict):
    # Get agent/skill activation request body
    api_endpoint = request_body["apiEndpoint"]
    project = request_body["projectId"]
    token = request_body["token"]
    experiment_name = request_body["payload"]["experiment_name"]
    instance = request_body["payload"]["instance"]

    # Create Cortex client and get experiment
    client = Cortex.client(api_endpoint=api_endpoint, project=project, token=token)
    experiment = Experiment(client.experiments.get_experiment(experiment_name), client.experiments)

    # Get model from last experiment run
    exp_run = experiment.last_run()
    model = exp_run.get_artifact('model')

    # Return model predict
    return {'payload': model.predict(instance).tolist()}
