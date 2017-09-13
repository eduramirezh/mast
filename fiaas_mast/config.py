import os


class Config(object):
    def __init__(self):
        self.PORT = os.environ.get('PORT', 5000)
        self.DEBUG = os.environ.get('DEBUG', False)
        self.APISERVER_TOKEN = self.get_apiserver_token()
        self.APISERVER_CA_CERT = self.get_apiserver_cert()

        self.ARTIFACTORY_USER = os.environ.get('ARTIFACTORY_USER')
        self.ARTIFACTORY_PWD = os.environ.get('ARTIFACTORY_PWD')
        if self.ARTIFACTORY_USER is None or self.ARTIFACTORY_PWD is None:
            raise RuntimeError(
                'You need to pass the \'ARTIFACTORY_USER\' and \'ARTIFACTORY_PWD\' environment variables')

    def get_apiserver_token(self):
        token = os.environ.get('APISERVER_TOKEN')
        if token is None:
            token_path = "/var/run/secrets/kubernetes.io/serviceaccount/token"
            if os.path.exists(token_path):
                with open(token_path) as fobj:
                    return fobj.read().strip()
            else:
                raise RuntimeError(
                    "Could not resolve apiserver token. No $APISERVER_TOKEN set in the environment and "
                    "{} did not exist.".format(token_path)
                )

        return token

    def get_apiserver_cert(self):
        cert = os.environ.get('APISERVER_CA_CERT')
        if cert is None:
            ca_cert_path = "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
            if os.path.exists(ca_cert_path):
                return ca_cert_path
            else:
                raise RuntimeError(
                    "Could not resolve apiserver CA certificate. No $APISERVER_CA_CERT set in the "
                    "environment and {} did not exist.".format(ca_cert_path)
                )

        return cert
