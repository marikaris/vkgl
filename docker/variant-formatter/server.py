import hgvs.dataproviders.uta
from hgvs.parser import Parser
from Babelfish import Babelfish
import hgvs2vcf
import json
import web

parser = Parser()

urls = (
    '/h2v', 'h2v'
)

class h2v:
    def POST(self):
        hdp = hgvs.dataproviders.uta.connect()
        babelfish37 = Babelfish(hdp, assembly_name="GRCh37")
        
        variants = json.loads(web.data())
        result = [hgvs2vcf.h2v(babelfish37, parser.parse_hgvs_variant(variant)) for variant in variants]
        return json.dumps(result)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()