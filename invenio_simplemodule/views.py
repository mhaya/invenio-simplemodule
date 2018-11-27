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
