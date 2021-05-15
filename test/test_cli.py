from click.testing import CliRunner
from k8s.__main__ import tables
from unittest.mock import Mock,patch
import datetime
import pdb

@patch('kubernetes.client.AppsV1Api')
def test_show(v1):
    v1.return_value=Mock(ok=True)
    v1.return_value.list_deployment_for_all_namespaces.return_value=[]

    runner = CliRunner()
    result = runner.invoke(tables,["show"])
    v1.assert_called_once()
    v1.list_deployment_for_all_namespaces.assert_called_once()

@patch('kubernetes.client.AppsV1Api')
def test_show_2(v1):
    v1.return_value=Mock(ok=True)
    v1.return_value.list_namespaced_deployment.return_value=[]

    runner = CliRunner()
    result = runner.invoke(tables,["show","--namespace=test"])
    v1.assert_called_once()
    v1.list_namespaced_deployment.assert_called_once()