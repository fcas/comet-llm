# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at https://www.comet.com
#  Copyright (C) 2015-2023 Comet ML INC
#  This source code is licensed under the MIT license found in the
#  LICENSE file in the root directory of this package.
# *******************************************************

from comet_ml import api

Duration = lambda: api.Metric("duration")  # noqa: E731
UserFeedback = lambda: api.Metric("user_feedback")  # noqa: E731
Timestamp = lambda: api.Metadata("start_server_timestamp")  # noqa: E731
TraceMetadata = api.Parameter
TraceDetail = api.Metadata
Other = api.Other
Tag = api.Tag
