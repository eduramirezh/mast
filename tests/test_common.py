#!/usr/bin/env python
# -*- coding: utf-8

# Copyright 2017-2019 The FIAAS Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from k8s.client import NotFound
from mock import patch

from fiaas_mast.common import check_models, PlatformError
from fiaas_mast.fiaas import FiaasApplication, FiaasApplicationSpec


class TestSelectModel:
    @pytest.fixture(params=(True, False))
    def crd(self, request):
        with patch('fiaas_mast.fiaas.FiaasApplication.list') as fm:
            fm.side_effect = None if request.param else NotFound()
            yield request.param

    @staticmethod
    def test_select_models(crd):
        if not crd:
            with pytest.raises(PlatformError):
                check_models()
            return

        wanted_app, wanted_spec = FiaasApplication, FiaasApplicationSpec
        actual_app, actual_spec = check_models()
        assert wanted_app == actual_app
        assert wanted_spec == actual_spec
