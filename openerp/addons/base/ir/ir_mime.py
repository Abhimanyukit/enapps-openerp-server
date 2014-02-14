# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv,fields
from osv.orm import except_orm


class ir_mime(osv.osv):

    _name = 'ir.mime'

    _rec_name = 'mime'
    _columns = {
        'mime': fields.char('MIME', size=512, required=True),
        'extension': fields.char('Extension', size=128, required=True, ),
    }
    
    def get_mime(self, cr, uid, file_name, context={}):
        file_extension = file_name.strip().split(".")
        if file_extension:
            file_extension = file_extension[-1]
            cr.execute('''SELECT mime FROM ir_mime WHERE extension ilike %s''', ("%%%s%%" % file_extension, ))
            for mime, in cr.fetchall():
                return mime
        return 'application/octet-stream'

ir_mime()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
