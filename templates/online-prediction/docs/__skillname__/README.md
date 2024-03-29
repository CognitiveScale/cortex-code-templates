# Online Prediction Skill

Long running Cortex skill serving REST API prediction requests for an example model

Note:
> This project assumes a `fast api server` with one endpoint `/invoke` that is run with the Uvicorn python3 binary; you may change to another framework or language.

## Building and Publishing the Skill

### Using the cortex cli

Building skill(s)

```
cortex workspaces build
```

Publishing  skill and docker image

```
cortex workspaces publish
```

### Using the VS code extension (CognitiveScale.cortex-code)

In order to build the daemon skill Docker image, simply select "Build Skills" from the Cortex menu in the IDE.  You can also right-click on the `skill.yaml` file for the skill and select "Build Skill" from the Cortex context menu.

Once the skill is built, you can publish it the same way, by selecting "Publish".
