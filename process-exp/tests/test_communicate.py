import subprocess
import pytest
import unittest


class CommunicateTest(unittest.TestCase):

	@pytest.mark.timeout(2)
	def test_subprocesses_parallel(self):
		processes = [ subprocess.Popen([ "sleep", "1" ], stdout = subprocess.PIPE, stderr = subprocess.PIPE, close_fds = True)  for i in range(0, 8) ]
		for p in processes:
			out, err = p.communicate()
		print(processes)

