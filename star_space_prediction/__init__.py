import pexpect
import re


class StarSpace(object):
    def __init__(self, exec_path, model_path, k=1, baseDocs=""):
        cmd = '{} {} {} {}'.format(exec_path, model_path, k, baseDocs)
        self.child = pexpect.spawn(cmd)
        self.child.expect('Enter some text: ')

    def predict(self, text):
        self.child.sendline(text)
        self.child.expect('Enter some text: ')
        stdout = self.child.before.decode('utf-8')
        lines = stdout.split('\n')
        results = []
        for line in lines:
            search = re.search(r'(\d)\[(\d+\.\d+)\]:\s(.*)\s+', line)
            if search:
                label = search.group(3).strip()
                proba = float(search.group(2).strip())
                results.append(dict(label=label, proba=proba))
        return results


if __name__ == "__main__":
    sp = StarSpace('/Starspace/query_predict', '/tmp/starspace/models/ag_news')
    print(sp.predict('The euro is up against the dollar'))
