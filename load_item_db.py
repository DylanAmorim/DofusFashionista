#!/usr/bin/env python3.5

# Copyright (C) 2020 The Dofus Fashionista
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import os

from fashionistapulp.fashionista_config import get_items_db_path, get_items_dump_path

def main():
    items_db_path = get_items_db_path()
    dumped_db_path = get_items_dump_path()
    os.system('rm %s' % items_db_path)
    os.system('sqlite3 %s < %s' % (items_db_path, dumped_db_path))
    os.system('chmod 666 %s' % items_db_path)

if __name__ == '__main__':
    main()
