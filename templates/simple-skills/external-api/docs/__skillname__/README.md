# {{skillname}} External API Skill (UPDATE THIS FOR YOUR SKILL)

A system generated Skill based on the custom external API Skill template. This skill type allows users to wrap an external REST API as a Cortex Fabric Skill.

> Modify these sections for your specific use case.


## Files Generated
- `docs/` - The directory that houses the Skills' READMEs
  - `{{skillname}}/`: The directory that houses the {{skillname}} Skill's README
    - `README.md`: Provide the objectives, requirements, and instructions for generating and deploying the Skill here.
- `skills/`: The directory that houses the Skills
  - `{{skillname}}/`: The directory that houses the {{skillname}} Skill's assets
    - `invoke/`: Contains the payloads, organized by Skill input name, used to invoke the {{skillname}} Skill
      - `request/`: Contains payload files used to invoke the Skill
        - `message.json`: Write a test JSON payload to invoke the Skill
      - `skill.yaml`: Define {{skillname}} Skill definition and map Actions here


## Generate the Skill

You've already done this via:
- [VS Code Extension](https://cognitivescale.github.io/cortex-code/)
- [Skill Builder in the Fabric Console](https://cognitivescale.github.io/cortex-fabric/docs/build-skills/skill-builder-ui)

Please use the above links for more information on how to continue building, pushing, deploying, developing, and invoking your Skill.

> NOTE: Modify the following files for your specific use case:
> - `docs/{{skillname}}/README.md`
> - `skills/{{skillname}}/actions/skill.yaml`
>   - Required Properties: `url`, `path`, `method`, and `headers.content-type` per the targeted external API
>   - Optional Properties: `headers.authorization`
> - `invoke/request/message.json`


## Test the code locally

To avoid filling your private registry, testing your code prior to deployment is recommended. Here's a way to do that.

### Create Python virtual env
```shell
python -m venv testvenv
source testvenv/bin/activate
pip install -r requirements.txt
```

### Test the Skill
```shell
python ./main.py '{"payload":{"message":  "This is a test payload message"}}'
````
Response:
```text
{"message":  "This is a test payload message"}
```

## Documentation
- [Cortex Fabric Documentation - Development - Develop Skills](https://cognitivescale.github.io/cortex-fabric/docs/development/define-skills)
- [Skill Elements](https://cognitivescale.github.io/cortex-fabric/docs/build-skills/define-skills#skill-elements)
- 