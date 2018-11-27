# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 mhaya.
#
# Invenio-SimpleModule is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask

from invenio_simplemodule import InvenioSimpleModule


def test_version():
    """Test version import."""
    from invenio_simplemodule import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioSimpleModule(app)
    assert 'invenio-simplemodule' in app.extensions

    app = Flask('testapp')
    ext = InvenioSimpleModule()
    assert 'invenio-simplemodule' not in app.extensions
    ext.init_app(app)
    assert 'invenio-simplemodule' in app.extensions

    app = Flask('testapp')
    ext = InvenioSimpleModule()
    app.config.update(
        BASE_TEMPLATE='invenio_theme/page.html'
    )
    ext.init_app(app)
    assert app.config['SIMPLEMODULE_BASE_TEMPLATE'] \
        == app.config['BASE_TEMPLATE']


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to Invenio-SimpleModule' in str(res.data)
