# -*- coding: utf-8 -*-
import uuid as _uuid
from Products.CMFCore.utils import getToolByName
from zope.component.hooks import getSite

def force_hex_uuid(uuid):
    """Return the UUID as a 32-character hexadecimal string."""
    try:
        return uuid.hex
    except AttributeError:
        return _uuid.UUID(uuid).hex



def uuidToPhysicalPath(uuid):
    """Given a UUID, attempt to return the absolute path of the underlying
    object. Will return None if the UUID can't be found.
    """

    uuid = force_hex_uuid(uuid)
    brain = uuidToCatalogBrain(uuid)
    if brain is None:
        return None

    return brain.getPath()


def uuidToURL(uuid):
    """Given a UUID, attempt to return the absolute URL of the underlying
    object. Will return None if the UUID can't be found.
    """

    uuid = force_hex_uuid(uuid)
    brain = uuidToCatalogBrain(uuid)
    if brain is None:
        return None

    return brain.getURL()


def uuidToObject(uuid):
    """Given a UUID, attempt to return a content object. Will return
    None if the UUID can't be found.
    """

    uuid = force_hex_uuid(uuid)
    brain = uuidToCatalogBrain(uuid)
    if brain is None:
        return None

    return brain.getObject()


def uuidToCatalogBrain(uuid):
    """Given a UUID, attempt to return a catalog brain.
    """

    site = getSite()
    if site is None:
        return None

    catalog = getToolByName(site, 'portal_catalog', None)
    if catalog is None:
        return None

    uuid = force_hex_uuid(uuid)
    result = catalog(UID=uuid)
    if len(result) != 1:
        return None

    return result[0]
