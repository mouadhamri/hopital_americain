# -*- coding: utf-8 -*-

from odoo.tools.mimetypes import guess_mimetype
from odoo import api, fields, models, _
from PIL import Image, ExifTags
import logging
import io

_logger = logging.getLogger(__name__)


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def _file_read(self, fname):
        full_path = self._full_path(fname)
        try:
            with open(full_path, 'rb') as f:
                data = f.read()
                try:
                    mimetype = guess_mimetype(data)
                    if mimetype.startswith('image/'):
                        image = Image.open(f)

                        for orientation in ExifTags.TAGS.keys():
                            if ExifTags.TAGS[orientation] == 'Orientation':
                                break

                        exif = image._getexif()

                        if exif and exif[orientation] == 3:
                            image = image.rotate(180, expand=True)
                        elif exif and exif[orientation] == 6:
                            image = image.rotate(270, expand=True)
                        elif exif and exif[orientation] == 8:
                            image = image.rotate(90, expand=True)

                        buf = io.BytesIO()
                        image.save(buf, format=mimetype.split('/')[1])
                        buf.seek(0)
                        data = buf.read()

                except (AttributeError, KeyError, IndexError):
                    # cases: image don't have getexif
                    pass
                return data
        except (IOError, OSError):
            _logger.info("_read_file reading %s", full_path, exc_info=True)
        return b''
