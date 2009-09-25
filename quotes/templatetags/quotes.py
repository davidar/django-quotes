# Copyright (C) 2009  David Roberts <d@vidr.cc>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
import cgi

from django import template

from quotes_config import quotes

register = template.Library()

@register.simple_tag
def random_quote():
    quote, author, url = random.choice(quotes)
    quote = quote.encode('ascii', 'xmlcharrefreplace')
    author = cgi.escape(author, True)
    url = cgi.escape(url, True)
    return """
    <p>%s</p>
    <p style="text-align:right">
        &mdash; <a href="%s">%s</a>
    </p>
    """ % (quote, url, author)
