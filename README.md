# Cloud Profiler for Cloud Run

How-to guide: Using Cloud Profiler in Cloud Run, using a minimum Python Flask webapp.

The official Google Cloud docs only list GCE, GKE, App Engine, and outside Google Cloud as available app deployment environments for using Cloud Profiler.
This repository wants to explore if and how Cloud Profiler can be used in Cloud Run.

For this purpose, a Python Flask webapp will be used.

## Maintainer

- Marcos Manuel Ortega - Director @ Indavelopers
- Consultant, architect & trainer
- Google Developer Expert - Google Cloud, modern infrastructure
- Google Cloud Authorized Trainer
- <info@indavelopers.com>
- LinkedIn: [linkedin.com/in/marcosmanuelortega](https://www.linkedin.com/in/marcosmanuelortega/)
- Made with ❤️ from Almería, Spain

## Documentation

- <https://cloud.google.com/profiler/docs/profiling-python>
- <https://cloud.google.com/profiler/docs/profiling-external>

## Before you begin

- Have a working Google Cloud project, linked to a working billing account
- Use Cloud Shell or a initialized and authenticated local Cloud SDK installation
  - Set the GCP project config with `PROJECT_ID`: `gcloud config set PROJECT_ID`
- Enable the required Google Cloud APIs:
  - Cloud Run Admin API
  - Artifact Registry API
  - Cloud Profiler Admin API
- Required roles:
  - Cloud Run Admin
  - Artifact Registry Administrator
  - Cloud Profiler User

## Usage

## License

MIT License (see `LICENSE` file).

## Known issues

Tested at the time of the last commit:

- None

If you find any issues, please open a GitHub issue, open a PR with a fix, or contact the maintainer.

## Contributions, help and discussion

Please, open an issue, submit a pull request, or generally contact the author by any means.

## TO-DOs

- Check min Python version for Cloud Profiler (3.11)
- Check error when installing Cloud Profiler python package from PyPI
- Check support for Cloud Run functions
- Check support for Cloud Run jobs
