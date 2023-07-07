from email_totals import ses

import os

from botocore.stub import Stubber


def test_send_email(mocker, mock_ses_response):
    recipient = 'user@synapse.org'
    text_body = 'test'
    html_body = '<html>test</html>'

    env_vars = {
            'SENDER': 'test@example.com',
    }
    mocker.patch.dict(os.environ, env_vars)

    with Stubber(ses.ses_client) as _stub:
        _stub.add_response('send_email', mock_ses_response)

        ses.send_report_email(recipient, html_body, text_body)
        # assert no exception is raised