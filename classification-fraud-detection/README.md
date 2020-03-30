# Instructions


1. Create a AI platform notebook instance.

   Enable the notebooks API (if not enabled already)

   First time starting an instance will take a short time, once created connect to it with the provided URL.

2. Open a terminal in the notebook session and clone the git repository:

   ```sh
   git clone https://github.com/nfaggian/ml-examples.git
   ```

3. Retrieve and review modelling data by executing the notebooks in: **solution-0-setup**

4. Each solution is self contained where:

    * **solution-1-services** demonstrates big-query ML
    * **solution-2-service-composition** demonstrates how to use AI platform training and prediction for a scikit-learn model
    * **solution-3-pipeline-orchestration** demonstrates how to build a kubeflow pipeline and use AI platform training and prediction
    * **solution-4-pipeline-package** demonstrates how to build a package that can be used to continuously deploy updated pipelines.
