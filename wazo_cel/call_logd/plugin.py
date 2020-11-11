# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import logging

from wazo_auth_client import Client as AuthClient
from wazo_call_logd.database.helpers import new_db_session
from wazo_call_logd.database.queries.base import BaseDAO
from xivo_dao.alchemy.cel import CEL as CELSchema

from .http import CELResource

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        api = dependencies['api']
        config = dependencies['config']
        auth_client = AuthClient(**config['auth'])
        dao = CELDAO(new_db_session(config['db_uri']))
        cel_service = CELService(dao)

        api.add_resource(
            CELResource,
            '/cel',
            resource_class_args=[auth_client, cel_service],
        )

    def set_default_tenant_uuid(self, token):
        self._cel_service.set_service_tenant_uuid(token['metadata']['tenant_uuid'])


class CELService:
    def __init__(self, cel_dao):
        self._cel_dao = cel_dao
        self._service_tenant_uuid = None

    def list(self, search_params):
        cel = self._cel_dao.find_all(search_params)
        return cel

    def set_service_tenant_uuid(self, tenant_uuid):
        self._service_tenant_uuid = tenant_uuid


class CELDAO(BaseDAO):
    def find_all(self, params):
        with self.new_session() as session:
            query = session.query(CELSchema)
            query = query.order_by(CELSchema.id.asc())
            if params.get('idbeg'):
                query = query.filter(CELSchema.id >= params['idbeg'])
            if params.get('limit'):
                query = query.limit(params['limit'])

            cdrs = query.all()
            session.expunge_all()
        return cdrs or []
