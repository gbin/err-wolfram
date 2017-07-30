import os

import wolframalpha

from errbot import BotPlugin, botcmd


class WolframAlpha(BotPlugin):
    """
    Query the Computational Knowledge Engine
    """

    def activate(self):
        super().activate()
        if self.config is not None:
            self.client = wolframalpha.Client(self.config['WA_TOKEN'])
        else:
            self.client = None

    def get_configuration_template(self):
        return {'WA_TOKEN': '49UVXJ-VPL9XLVKAH',
               }

    @botcmd
    def wa(self, msg, arg):
        """
        Query Wolfram Alpha, the Computational Knowledge Engine.
        """
        if self.client is None:
            return 'This plugin needs to be configured.'

        ans = ''
        res = self.client.query(arg)
        try:
            for pod in res.pods:
                if pod.title in ['Result', 'Results']:
                    for sub in pod.subpods:
                        ans += sub.plaintext
        except AttributeError:
            self.log.error('KeyError triggered on retrieving pods.')
        return ans if ans else 'Dunno ¯\\_(ツ)_/¯'
