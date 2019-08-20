# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 mhaya.
#
# Invenio-SimpleModule is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio msimple module that is developed in training."""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from __future__ import absolute_import, print_function

from flask import Blueprint, render_template
from flask_babelex import gettext as _
from invenio_app.factory import instance_path, static_folder
import os

blueprint = Blueprint(
    'invenio_simplemodule',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route("/")
def index():
    """Render a basic view."""
    return render_template(
        "invenio_simplemodule/index.html",
        module_name=_('Invenio-SimpleModule'))


@blueprint.route('/env')
def hello():
    L = []
    L.append("<h1>os.environ.items()</h1>")
    for k, v in os.environ.items():
        L.append("{key} : {value}".format(key=k, value=v))

    
    L.append("<h1>invenio_app()</h1>")
    L.append("instance_path:"+instance_path)
    L.append("static_folder:"+static_folder)

    L.append("<h1>flask_current_app</h1>")
    for k, v in flask_current_app.config.items():
        L.append("{key} : {value}".format(key=k, value=v))

    return "</br>".join(L)
