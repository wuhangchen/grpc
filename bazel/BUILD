# Copyright 2017 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Contains build targets used by Starlark files in the bazel/ directory.
"""

licenses(["notice"])

package(default_visibility = ["//:__subpackages__"])

filegroup(
    name = "_single_module_tester",
    srcs = ["_single_module_tester.py"],
)

filegroup(
    name = "_gevent_test_main",
    srcs = ["_gevent_test_main.py"],
)

filegroup(
    name = "_logging_threshold_test_main",
    srcs = ["_logging_threshold_test_main.py"],
)
