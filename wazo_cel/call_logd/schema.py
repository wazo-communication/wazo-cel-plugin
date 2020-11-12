# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from marshmallow import (
    EXCLUDE,
    fields,
    Schema,
)
from marshmallow.validate import Length, Range


class CELListRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    idbeg = fields.String(validate=Length(min=1))
    limit = fields.Integer(validate=Range(min=0), missing=1000)
    linkedid = fields.String(validate=Length(min=1))


class CELSchema(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    id = fields.String()
    eventtype = fields.String()
    eventtime = fields.String()
    userdeftype = fields.String()
    cid_name = fields.String()
    cid_num = fields.String()
    cid_ani = fields.String()
    cid_rdnis = fields.String()
    cid_dnid = fields.String()
    exten = fields.String()
    context = fields.String()
    channame = fields.String()
    appname = fields.String()
    appdata = fields.String()
    amaflags = fields.String()
    accountcode = fields.String()
    peeraccount = fields.String()
    uniqueid = fields.String()
    linkedid = fields.String()
    userfield = fields.String()
    peer = fields.String()
    call_log_id = fields.String()
    extra = fields.String()
