import os
import subprocess
import sys

import fire
import pickle
import numpy as np
import pandas as pd

import hypertune

from sklearn.metrics import roc_auc_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


def train_evaluate(
    job_dir,
    training_dataset_path,
    validation_dataset_path,
    max_depth,
    n_estimators,
    hptune,
):

    df_train = pd.read_csv(training_dataset_path)
    df_validation = pd.read_csv(validation_dataset_path)

    if not hptune:
        df_train = pd.concat([df_train, df_validation])

    numeric_feature_indexes = slice(0, 30)

    preprocessor = ColumnTransformer(
        transformers=[("num", StandardScaler(), numeric_feature_indexes),]
    )

    pipeline = Pipeline(
        [("preprocessor", preprocessor), ("classifier", RandomForestClassifier()),]
    )

    num_features_type_map = {
        feature: "float64" for feature in df_train.columns[numeric_feature_indexes]
    }

    df_train = df_train.astype(num_features_type_map)
    df_validation = df_validation.astype(num_features_type_map)

    X_train = df_train.drop("Class", axis=1)
    y_train = df_train["Class"]

    pipeline.set_params(
        classifier__max_depth=max_depth, classifier__n_estimators=n_estimators
    )

    pipeline.fit(X_train, y_train)

    if hptune:
        X_validation = df_validation.drop("Class", axis=1)
        y_validation = df_validation["Class"]

        y_pred_proba = pipeline.predict_proba(X_validation)[::, 1]
        auc = roc_auc_score(y_validation, y_pred_proba)

        print("Model roc_auc: {}".format(auc))

        # Log it with hypertune
        hpt = hypertune.HyperTune()
        hpt.report_hyperparameter_tuning_metric(
            hyperparameter_metric_tag="roc_auc", metric_value=auc
        )

    # Save the model
    if not hptune:
        model_filename = "model.pkl"
        with open(model_filename, "wb") as model_file:
            pickle.dump(pipeline, model_file)
        gcs_model_path = "{}/{}".format(job_dir, model_filename)
        subprocess.check_call(
            ["gsutil", "cp", model_filename, gcs_model_path], stderr=sys.stdout
        )
        print("Saved model in: {}".format(gcs_model_path))


if __name__ == "__main__":
    fire.Fire(train_evaluate)
