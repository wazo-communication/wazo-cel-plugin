# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from flask import request
from xivo.auth_verifier import required_acl
from wazo_call_logd.rest_api import AuthResource

from .schema import (
    CELListRequestSchema,
    CELSchema,
)


class CELResource(AuthResource):
    def __init__(self, auth_client, cel_service):
        super().__init__()
        self.cel_service = cel_service
        self.auth_client = auth_client

    @required_acl('call-logd.cel.read')
    def get(self):
        args = CELListRequestSchema().load(request.args)
        cels = self.cel_service.list(args)
        return CELSchema().dump(cels, many=True)
