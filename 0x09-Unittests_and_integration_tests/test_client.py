#!/usr/bin/env python3
"""This module contais the test for the GithubOrgClient class
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json


class TestGithubOrgClient(unittest.TestCase):
    """test for the GithubOrgClient class
    """
    @parameterized.expand([
        ('google', 'Hola'),
        ('abc', 'Hola')
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mocked):
        """test the GithubOrgClient.org method
        """
        mocked.return_value = expected
        github_org_client = GithubOrgClient(org)

        self.assertEqual(github_org_client.org, expected)
        mocked.assert_called_once()

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_public_repos_url(self, org):
        """test the GithubOrgClient._public_repos_url method
        """
        github_org_client = GithubOrgClient(org)
        expected_url = 'https://api.github.com/orgs/{}/repos'.format(org)
        expected = {"repos_url": expected_url}

        prop = 'client.GithubOrgClient.org'
        with patch(prop, new_callable=PropertyMock) as mocked:
            mocked.return_value = expected
            value = expected["repos_url"]
            self.assertEqual(github_org_client._public_repos_url, value)

    @patch('client.get_json')
    def test_public_repos(self, mocked):
        """test the GithubOrgClient.public_repos method
        """
        expected = [{"name": "repo1"}, {"name": "repo2"}]
        expected1 = ["repo1", "repo2"]
        org = "google"
        mocked.return_value = expected

        github_org_client = GithubOrgClient(org)
        prop = 'client.GithubOrgClient._public_repos_url'
        with patch(prop, new_callable=PropertyMock) as prop_mocked:
            prop_mocked.return_value = expected1
            self.assertEqual(github_org_client.public_repos(), expected1)
            mocked.assert_called_once()
            prop_mocked.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """test the GithubOrgClient.has_license method
        """
        org = "google"
        github_org_client = GithubOrgClient(org)

        self.assertEqual(
            github_org_client.has_license(repo, license_key),
            expected
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient class
    """
    @classmethod
    def setUpClass(cls):
        """setUpClass class method
        """
        requests_json = unittest.mock.Mock()
        # in each call return a value
        # first call requests.get return cls.org_payload
        # second call response.json return cls.repos_payload
        requests_json.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload,
        ]

        cls.get_patcher = patch('requests.get', return_value=requests_json)
        cls.get_patcher.start()

    def test_public_repos(self):
        """test the GithubOrgClient.public_repos method
        """
        org = "google"
        github_org_client = GithubOrgClient(org)

        self.assertEqual(github_org_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """test the GithubOrgClient.public_repos method with a licence
        """
        org = "google"
        github_org_client = GithubOrgClient(org)

        self.assertEqual(
            github_org_client.public_repos("apache-2.0"),
            self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls):
        """tearDownClass class method
        """
        cls.get_patcher.stop()
