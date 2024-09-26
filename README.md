# jobrunner

## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.

## jobRunner

## Features to Support

- Creation of a job object
- ability to import settings
- export settings to a TOML
- export settings to a Mark down report
- Create MJB files for a job
- Organize the output from Mail Manager
- Handle Jobs with Multiple Mailings
- Handle Jobs with Multiple Mailings that Also have multiple CRIDS
- infer container type

## Settings to Import

### Meta data

- Job Number
- Client Name
- Job Folder Path

### Job Data

- Mail Class (STD, FCM, NP)
- Postage Type (stamp, permit)
- Due Date
- CRID
- Content of mail (political)

### Data Manipulation

- CASS
- NCOA
- DSF
- Vacant
- Bad Record handling
- Deduping (Name, Address, Exact)

### Presort Specs

- Length
- Height
- Thickness
- Catagory (letter, flat, parcel)
