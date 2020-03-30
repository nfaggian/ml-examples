# ML Examples

Short ml examples for data scientists using Google Cloud Platform (GCP).

## Tasks

- Identify fraudulent transactions in a credit transaction database [[code]](https://github.com/nfaggian/ml-examples/tree/master/classification-fraud-detection)

## Methodology

The approach followed while solving the ML task adopts the following increasing levels of complexity.

**Low complexity; service use**

- Training and prediction (BQML)

**Moderate complexity; composition of services**

- Notebooks parameterizing jobs on Cloud AI Platform (CAIP)
- Traininng and Prediction using CAIP

**Intermediate complexity; pipeline orchestration of services**

- Notebooks parameterizing pipelines
- Traininng and Prediction using CAIP
- Pipeline orchestration using kubeflow

**High complexity; automated orchestration of a CT/CD pipeline**

- Pipelines as packaged software
- Custom training pipeline (kubeflow)
- Custom prediction service (cloud functions, cloud run)
- Continuous training, deployment (cloud build)
