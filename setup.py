#
# Copyright 2020 The dNation Jsonnet Translator Authors. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from setuptools import setup, find_packages


install_requires = [
    "jsonnet==0.16.*",
    "kubernetes==12.0.*",
    "patool==1.12",
    "urllib3==1.25.*",
    "tenacity==6.3.*",
    "python-json-logger==2.0.*",
]


setup(
    name="kubernetes-jsonnet-translator",
    description="Generates json resources from jsonnet resources",
    author="dnation",
    author_email="david.suba@dnation.cloud",
    version="0.3.0",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=["black", "flake8"],
)
