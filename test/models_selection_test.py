from __future__ import absolute_import, division, unicode_literals
import unittest

import mock

import cola.models.selection as selection


class SelectionTestCase(unittest.TestCase):

    def test_union(self):
        t = mock.Mock()
        t.staged = ['a']
        t.unmerged = ['a', 'b']
        t.modified = ['b', 'a', 'c']
        t.untracked = ['d']

        expect = ['a', 'b', 'c', 'd']
        actual = selection.union(t)
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
