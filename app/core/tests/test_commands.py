"""
test custom django management command to wait for the database to be available.
"""
# for mocking db behaviour 
from unittest.mock import patch
# OperationalError for db state
from psycopg2 import OperationalError as Psycopg2Error

# helper functions for django management commands
from django.core.management import call_command
# OperationalError for simulating db unavailability thrown by database backends
from django.db.utils import OperationalError
from django.test import SimpleTestCase

# this is check method we declare in /core/management/commands/wait_for_db file 
# check method is provided by BaseCommand class
# mocking the connection check method to simulate db availability
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Tests for wait_for_db command."""

    def test_wait_for_db_ready(self,patched_check):
        """Test waiting for db when db is ready."""
        # simulating db being available immediately
        patched_check.return_value = True

        # call the wait_for_db command
        call_command('wait_for_db')

        # assert that the check method was called exactly once
        patched_check.assert_called_once_with(databases=['default'])
        
    
    @patch('time.sleep')
    def test_wait_for_db_ready(self,patched_sleep,patched_check):
        """Test waiting for db when db is unavailable initially."""
        # simulating db being unavailable initially

        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        # call the wait_for_db command
        call_command('wait_for_db')

        # assert that the check method was called 6 times (5 failures + 1 success)
        self.assertEqual(patched_check.call_count,6)
        patched_check.assert_called_with(databases=['default'])
        