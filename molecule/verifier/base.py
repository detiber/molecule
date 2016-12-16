#  Copyright (c) 2015-2016 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import abc

from molecule import util


class Base(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, molecule):
        """
        Base initializer for all :ref:`Verifier` classes.

        :param molecule: An instance of molecule.
        :returns: None
        """
        self._molecule = molecule
        self.errors = ""
        self.warnings = ""

        def error_callback(msg):
            util.print_error(msg, pretty=False)
            self.errors += msg

        def info_callback(msg):
            util.print_info(msg, pretty=False)

        self._error_callback = error_callback
        self._info_callback = info_callback

    @abc.abstractproperty
    def execute(self):  # pragma: no cover
        pass
