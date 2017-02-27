# Copyright 2016 Google Inc. All Rights Reserved. Licensed under the Apache
# License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""Tests for predict.py ."""
import base64

import pytest

from predict import census_to_example_bytes, predict_json


MODEL = 'census'
VERSION = 'v1'
PROJECT = 'python-docs-samples-tests'
JSON = {
    'age': 25,
    'workclass': ' Private',
    'education': ' 11th',
    'education_num': 7,
    'marital_status': ' Never-married',
    'occupation': ' Machine-op-inspct',
    'relationship': ' Own-child',
    'race': ' Black',
    'gender': ' Male',
    'capital_gain': 0,
    'capital_loss': 0,
    'hours_per_week': 40,
    'native_country': ' United-States'
}
EXPECTED_OUTPUT = {
    u'probabilities': [0.9942260384559631, 0.005774002522230148],
    u'logits': [-5.148599147796631],
    u'classes': 0,
    u'logistic': [0.005774001590907574]
}


def test_predict_json():
    result = predict_json(PROJECT, MODEL, [JSON, JSON], version=VERSION)
    assert [EXPECTED_OUTPUT, EXPECTED_OUTPUT] == result


def test_predict_json_error():
    with pytest.raises(RuntimeError):
        predict_json(PROJECT, MODEL, [{"foo": "bar"}], version=VERSION)


# TODO(elibixby) Run on Travis when TensorFlow PyPi package supports
# Ubuntu 12.04 See:
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/g3doc/get_started/os_setup.md#import-error
@pytest.mark.slow
def test_census_example_to_bytes():
    b = census_to_example_bytes(JSON)
    assert base64.b64encode(b) is not None


def test_predict_tfrecord():
    # Using the same model for TFRecords and
    # JSON is currently broken.
    # TODO(elibixby) when b/35742966 is fixed add
    pass
