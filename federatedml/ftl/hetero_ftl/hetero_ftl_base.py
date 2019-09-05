#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from arch.api import federation
from federatedml.model_base import ModelBase
from federatedml.ftl.autoencoder import Autoencoder


class HeteroFTLParty(ModelBase):
    @staticmethod
    def _create_local_model(params):
        autoencoder = Autoencoder("local_host_model_01")
        autoencoder.build(input_dim=params.input_dim, hidden_dim=params.encode_dim,
                          learning_rate=params.learning_rate)
        return autoencoder

    def _do_remote(self, value=None, name=None, tag=None, role=None, idx=None):
        federation.remote(value, name=name, tag=tag, role=role, idx=idx)

    def _do_get(self, name=None, tag=None, idx=None):
        return federation.get(name=name, tag=tag, idx=idx)
